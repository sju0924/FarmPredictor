import {getRegion, init, addUser, addFavor,getFavor} from '../service/userService'

var db_init=async(req:any, res:any)=>{
    init();
}
//회원 가입
var add_user=async(req:any, res:any)=>{
    let data = await addUser(req.query.id, req.query.name, req.query.region, req.query.reg2);
    try{
        console.log(req.query)
        let data = await getRegion(req.query.id)
        res.setHeader("Access-Control-Allow-Origin", "*");
        res.setHeader("Access-Control-Allow-Credentials", "true");
        res.setHeader("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT");
        res.setHeader("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers");
        
        res.send({
            "msg":"회원 등록 완료",
            "success":true,
            "data": data
        });
        
       
    }
    catch{
        res.send(500);
    }  
    
}

var add_favor=async(req:any,res:any)=>{
    try{
        console.log("add favor:", req.query.id, req.query.crop)
        let data = await addFavor(req.query.id, req.query.crop);
        res.send({
            "msg":"나의 작물 등록 완료",
            "success":true,
            "data": data
        });
    }
    catch(err){
        console.log(err)
        res.send(500);
}  

}
var get_region=async(req:any,res:any)=>{
    try{
        console.log(req.query)
        let data = await getRegion(req.query.id)
        res.setHeader("Access-Control-Allow-Origin", "*");
        res.setHeader("Access-Control-Allow-Credentials", "true");
        res.setHeader("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT");
        res.setHeader("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers");
        try{
            res.send({
                "msg":"조회 완료",
                "success":true,
                "data":data
            });
        }
        catch(err){
            console.log(err)
            res.send({
                "msg":"조회 실패",
                "success":false
            })
        }
       
    }
    catch{
        res.send(500);
    }  
    
}
var get_favor=async(req:any,res:any)=>{
    try{
        console.log(req.query)
        let data = await getFavor(req.query.id)
          
        res.send({
            "msg":"조회 완료",
            "success":true,
            "data":data
        });
        
       
    }
    catch{
        res.send(500);
    }  
    
}

export {get_region,db_init,add_user,add_favor, get_favor}