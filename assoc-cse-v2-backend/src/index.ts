import express from "express";

import { PORT } from "./config/constants";

// Import APIs here.
import api from "./routes/api";

const app: express.Application = express();

// Testing to see if this works or not.
app.use("/api", api);

app.listen(PORT, () => {
    console.log(`APP IS LISTENING ON PORT ${PORT}`);
});

console.log("FINAL TEST");