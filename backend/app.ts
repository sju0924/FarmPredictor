import express from "express"
import axios from "axios"
import { userdao } from "./src/dao/userdao";
import {Router} from './src/router/router';
import bodyParser from 'body-parser'
import dotenv from "dotenv"
import cors from 'cors'
dotenv.config();
const app = express();
app.use(bodyParser.json()); //json 형태로 parsing
app.use(bodyParser.urlencoded({ extended: false}));
app.use('/static', express.static('public'))
app.use(express.static('.'))
const corsOption={
    origin: "http://localhost:8000/",
    optionsSuccessStatus:200
};
app.use(cors(corsOption))
app.use('/',Router)

app.listen(process.env.BACKEND_PORT, () => {
    console.log("server run on port", process.env.BACKEND_PORT);
})