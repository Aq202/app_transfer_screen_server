const express = require("express")
const http = require("http");
const port = require("./services/port");
const SocketServer = require("./services/socketServer");
const fs = require('fs');
const { serverRouter } = require("./routes/server.route");


const app = express();
const httpServer = http.createServer(app);

new SocketServer(httpServer);

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(express.static(__dirname + "/public"));

app.use("/server", serverRouter)

app.get("/", (req, res) => {
    res.send(req.hostname)
})

app.post("/transfer", (req, res) => {

    const { imagePath } = req.body

    // Lee la imagen como un buffer
    const buffer = fs.readFileSync(imagePath);
    const base64 = buffer.toString('base64');
    SocketServer.send(base64)
    res.sendStatus(200)
})



httpServer.listen(port, () => console.log(`Servidor corriendo en puerto  ${port}.`))