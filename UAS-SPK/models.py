from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class tbl_hp(Base):
    __tablename__ = 'tbl_hp'
    nama_hp: Mapped[str] = mapped_column(primary_key=True)
    reputasi_brand: Mapped[int] = mapped_column()
    processor: Mapped[int] = mapped_column()
    baterai: Mapped[int] = mapped_column()
    harga: Mapped[int] = mapped_column()
    ukuran_layar: Mapped[int] = mapped_column()
    
    def __repr__(self) -> str:
        return f"tbl_hp(nama_hp={self.nama_hp!r}, reputasi_brand={self.reputasi_brand!r})"