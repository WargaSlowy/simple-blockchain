import hashlib as hasher
from datetime import datetime
from typing import Any


class Block:
    def __init__(
        self, indeks: int, cap_waktu: datetime, data: Any, hash_sebelumnya: str
    ) -> None:
        self.indeks: int = indeks
        self.cap_waktu: datetime = cap_waktu
        self.data: Any = data
        self.hash_sebelumnya: str = hash_sebelumnya

        self.hash_block = self._hitung_hash_block()

    def _hitung_hash_block(self) -> str:
        sha = hasher.sha256()
        isi_blok = (
            str(self.indeks)
            + str(self.cap_waktu)
            + str(self.data)
            + str(self.hash_sebelumnya)
        )

        sha.update(isi_blok.encode("utf-8"))
        return sha.hexdigest()


def buat_blok_genesis() -> Block:
    return Block(
        indeks=0,
        cap_waktu=datetime.now(),
        data="aku pencipta data digital paling pertama di dunia",
        hash_sebelumnya="0",
    )


def buat_blok_selanjutnya(blok_terakhir: Block) -> Block:
    indeks_baru: int = blok_terakhir.indeks + 1
    cap_waktu_baru: datetime = datetime.now()
    data_baru: str = f"hehey saya dari blok nomor {indeks_baru} rek, woilah cik"
    hash_blok_sebelumnya: str = blok_terakhir.hash_block

    return Block(
        indeks=indeks_baru,
        cap_waktu=cap_waktu_baru,
        data=data_baru,
        hash_sebelumnya=hash_blok_sebelumnya,
    )

if __name__ == "__main__":
    rantai_blok: list[Block] = [buat_blok_genesis()]
    blok_sebelumnya: Block = rantai_blok[0]

    jumlah_blok_yang_ditambah: int = 20

    for i in range(jumlah_blok_yang_ditambah):
        blok_baru: Block = buat_blok_selanjutnya(blok_sebelumnya)
        rantai_blok.append(blok_baru)
        blok_sebelumnya = blok_baru

        print(f"block data #{blok_baru.indeks} telah ditambahkan ke dalam jaringan blockchain")
        print(f"data hash: {blok_baru.hash_block}\n")
