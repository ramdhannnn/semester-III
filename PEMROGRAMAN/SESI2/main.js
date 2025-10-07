function hitungHargaAkhir(totalBelanja) {
  let diskon = 0;

  if (totalBelanja > 1000000) {
    diskon = 0.15;
  } else if (totalBelanja > 500000) {
    diskon = 0.10;
  }

  const hargaAkhir = totalBelanja - (totalBelanja * diskon);
  return hargaAkhir;
}

// Tambahkan ini supaya ada output
console.log(hitungHargaAkhir(1200000));