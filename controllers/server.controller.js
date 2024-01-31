const os = require("os");
const port = require("../services/port");
//const ip = require("../services/ip");

const getServerURL = (req, res) => {
	try {
		const networkData = os.networkInterfaces()["Wi-Fi"].find(network => network.family === "IPv4");
		const ip = networkData.address;

		res.send({ url: `http://${ip}:${port}` });
	} catch (ex) {
		console.log("Error al obtener ip del servidor: ", ex);
		res.statusMessage = "Ocurrio un error al obtener la Ip del servidor.";
		res.sendStatus(500);
	}
};

const getServerStatus = (req, res) => {
	res.send({ status: true });
};

exports.getServerURL = getServerURL;
exports.getServerStatus = getServerStatus;
