import { userdao } from "../dao/userdao";
import { userdto } from "../dto/userdto";

var getRegion=async(id:number)=>{
    let dao = new userdao();
    let dto = new userdto(id,"","","",[]);

    
    var data = await dao.get_region(dto);
    var res={
        'region':data,
        'count': data.length
    }
    return res;
}

var setRegion=async(id:number, region:number)=>{
    let dao = new userdao();
    
    var data = await dao.set_region();
    
    var ret={
        'success':false,
        'data':data
    }
    return ret;
}

var addUser=async(id:number, name:string, region:string,reg2:string)=>{
    let dao = new userdao();    
    let dto = new userdto(id,name,region,reg2,[]);
    var data = await dao.set_region(dto);
    
    var ret={
        'success':true,
        'data':data
    }
    return ret;
}

var addFavor=async(id:number, item:string)=>{
    let dao = new userdao();    
    var data= await dao.add_favor(id, item);
    var ret={
        'data':data
    }
    return ret;

}

var getFavor=async(id:number)=>{
    let dao = new userdao();
    let dto = new userdto(id,"","","",[]);     
    var data:any = await dao.get_favor(dto);
    var res:any=[]
    console.log(data);
    for(var i = 0 ; i<data.length;i++){
        res.push(data[i].crop);
    }
    return res;

}

var init=async()=>{
    let dao = new userdao();    
    var data = await dao.init();
    
    var ret={
        'success':true,
        'data':data
    }
    return ret;
}
export{getRegion, setRegion,init,addUser, addFavor, getFavor}