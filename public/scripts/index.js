

document.addEventListener('DOMContentLoaded', async () => {
    const qrcode = document.querySelector(".qrcode")
    const res = await fetch("/server/getServerURL")
    const result = await  res.json()
    new QRCode(qrcode, result.url);
})
