import express from "express"
import {get_region,db_init,add_user,add_favor,get_favor} from "../controller/controller"
const Router = express.Router();
Router.use(express.json()); //json 형태로 parsing
Router.use(express.urlencoded( {extended : false } )); 
Router.use('/static', express.static('public'))
Router.use(express.static('../../'))
//대시보드
Router.get('/dashboard',function(req:any,res:any){
    res.send("hello");
})

Router.post('/dashboard',function(req,res){
    console.log(req.body);
    res.send(req.body);
})
Router.get('/user/region',get_region);
Router.get('/init',db_init);
Router.get('/user/add', add_user);
Router.get('/user/add/favor',  add_favor);
Router.get('/user/favor',  get_favor);
export {Router}