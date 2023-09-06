
module.exports = class SocketServer {

    static io;

    constructor(server) {
        SocketServer.io = require("socket.io")(server);

        //this.executeMiddleWares()
        this.initServer()
    }


    initServer() {

        SocketServer.io.on("connection", socket => {
            console.log("Cliente conectado")


            socket.on("download-file", message => {
                socket.broadcast.emit("download-file    ", message)
            })

        });



    }

    static send(value) {
        //console.log("sending file")

        SocketServer.io.emit("download-file", value)
    }


}