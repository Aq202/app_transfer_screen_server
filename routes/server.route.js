const express = require("express");
const { getServerURL, getServerStatus } = require("../controllers/server.controller");

const router = express.Router();

router.get("/getServerURL", getServerURL);
router.get("/getServerStatus", getServerStatus);

exports.serverRouter = router;
