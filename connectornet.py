"""connectornet - küçük ağ yardımcıları

Basit, güvenli ve platform-bağımsız yardımcı fonksiyonlar sağlar:
- `connect_tcp` : TCP sunucu/porta bağlanır
- `start_tcp_server` : basit TCP server başlatır (thread ile)
- `send_tcp_message` / `recv_tcp_message` : socket üzerinden gönderme/alma
- `scan_ports` : TCP bağlantı denemesi ile port tarama
- `resolve_hostname` : DNS çözümleme
- `get_local_ip` : yerel IP alma

Bu modül, güvenlik ve yetki gerektiren ham ICMP işlemlerinden kaçınır;
"ping" benzeri kontroller için kısa TCP bağlantı denemeleri kullanır.
"""

from __future__ import annotations

import socket
import threading
from typing import Callable, Iterable, List, Optional, Tuple


def connect_tcp(host: str, port: int, timeout: float = 5.0) -> socket.socket:
    """TCP ile `host:port`'a bağlanıp bağlı socket döner. Hata durumunda istisna fırlatır.

    Kullanım: s = connect_tcp('example.com', 80)
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((host, port))
    return s


def send_tcp_message(sock: socket.socket, data: bytes) -> int:
    """Verilen socket'e tüm `data`'yı gönderir. Gönderilen byte sayısını döner."""
    return sock.sendall(data) or len(data)


def recv_tcp_message(sock: socket.socket, bufsize: int = 4096) -> bytes:
    """Socket'ten tek seferde veri okur; boş dönerse bağlantı kopmuştur."""
    return sock.recv(bufsize)


def start_tcp_server(host: str,
                     port: int,
                     handler: Callable[[socket.socket, Tuple[str, int]], None],
                     backlog: int = 5) -> threading.Thread:
    """Basit bir TCP server başlatır; her bağlantı için `handler(sock, addr)` çağrılır.

    Fonksiyon bir daemon `Thread` döner; thread'in canlı kalması için dönen thread üzerinde join yapılabilir.
    Handler içinde socket kapatma sorumluluğu kullanıcıdadır.
    """

    def server_thread():
        srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((host, port))
        srv.listen(backlog)
        try:
            while True:
                client, addr = srv.accept()
                t = threading.Thread(target=handler, args=(client, addr), daemon=True)
                t.start()
        finally:
            try:
                srv.close()
            except Exception:
                pass

    t = threading.Thread(target=server_thread, daemon=True)
    t.start()
    return t


def scan_ports(host: str, ports: Iterable[int], timeout: float = 0.5) -> List[int]:
    """Verilen port listesinde TCP bağlantı kurulabilenleri döner (açık portlar).

    Hafif ve hızlı bir tarama yapar; güvenlik duvarları/talanma korumaları göz önünde bulundurulmalıdır.
    """
    open_ports: List[int] = []
    for p in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((host, p))
            open_ports.append(p)
            s.close()
        except Exception:
            continue
    return open_ports


def resolve_hostname(name: str) -> List[str]:
    """Hostname'i çözümleyip IP listesi döner."""
    try:
        infos = socket.getaddrinfo(name, None)
        return list({info[4][0] for info in infos})
    except Exception:
        return []


def get_local_ip(dest: str = "8.8.8.8") -> Optional[str]:
    """Kısa bir UDP soketi ile yerel IP'yi tespit etmeye çalışır (internete çıkış arayüzü).

    Varsayılan hedef kullanılarak (ör. 8.8.8.8) en yaygın arayüz tespit edilir.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((dest, 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return None


if __name__ == "__main__":
    # Küçük bir demo: local IP ve örnek resolve
    print("connectornet demo")
    print("local ip:", get_local_ip() or "unknown")
    print("resolve localhost:", resolve_hostname("localhost"))
