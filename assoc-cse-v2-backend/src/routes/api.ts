import express from "express";

let api: express.Router = express.Router();

api.get("/", (_, res: express.Response) => {
    console.log("Root Trigerred");
    res.json({
        message: "Success"
    });
});

export default api;