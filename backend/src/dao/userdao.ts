import { userdto } from "../dto/userdto";
import dotenv from "dotenv"
import { conn } from "../utils/conn"
dotenv.config();
conn.connect();

class userdao{

    init:any = async()=>{
        let sql:string = 'CREATE TABLE user(id bigint PRIMARY KEY, name varchar(20), region varchar(20), reg2  varchar(20));'+
                            'CREATE TABLE favor(id int, crop varchar(40), PRIMARY KEY(id,crop));';
        let result = await conn.promise().query(sql);
        console.log(result);
    }
    //req: SID
    //res: serial, id, name
    //사용 테이블: usertable
    get_region:any=async(dto:userdto)=>{
        let sql:string = 'SELECT region, reg2 FROM user WHERE id = ? ';
        let [rows, fields] = await conn.promise().query(sql,[dto.get_id()]);
        console.log(rows)

        return rows
    }

    set_region:any=async(dto:userdto)=>{
        let sql:string = 'insert into user (id, name, region, reg2)  values(?,?,?,?);';
        let [result, fields] = await conn.promise().query(sql,[dto.get_id(),dto.get_name(),dto.get_region(),dto.get_region2()]);
        
        console.log(result);
        
        return result;
    }

    set_user:any=async(dto:userdto)=>{
        let sql:string = 'INSERT INTO user(id, name, region, reg2) VALUES(?,?,?,?);'
        let params=[dto.get_id(), dto.get_name(),dto.get_region(), dto.get_region2()]
    }
    
    get_favor:any = async(dto:userdto)=>{
        let sql:string = "SELECT crop FROM favor WHERE id = ?;";
        
        let [rows, fields] = await conn.promise().query(sql,[dto.get_id()]);
        return rows;
    }
    add_favor:any=async(id:number, newitem:string)=>{
        let item = [id, newitem];
        let sql ='INSERT INTO favor(id, crop) values(?,?)';
        let [rows, fields] = await conn.promise().query(sql,item);
        console.log(rows);
    }
}

export{userdao}