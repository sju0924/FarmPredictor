class userdto{
    id: number;
    name: string;
    region : string;
    reg2: string;
    favor: string[];

    constructor(id:number, name:string, region:string, reg2:string, favor:string[]){
        this.id = id;
        this.name= name;
        this.region= region,
        this.reg2= reg2,
        this.favor=favor;
    }
    
    set_id=(id:number)=>{
        this.id=id;
        return;
    }
    set_region=(region:string)=>{
        this.region=region;
        return;
    }
    set_favor=(favor:string[])=>{
        this.favor=favor;
        return;
    }
    get_id=()=>{
        var res:number = this.id;
        return res;
    }
    get_name=()=>{
        return this.name;
    }
    get_region=()=>{
        return this.region;
    }
    get_region2=()=>{
        return this.reg2;
    }
    get_favor=()=>{
        return this.favor;
    }
    print=()=>{
        console.log("====print DTO====");
        console.log("serial: ",this.id);
        console.log("name: ",this.name);
        console.log("id: ",this.region);
        for (var item in this.favor){
            console.log("favor: ",item);
        }
        console.log("=================");

    }
    getValue=()=>{
        return {
            "id": this.id,
            "name":this.name,            
            "studentID":this.region,
        }
    }
};

export {userdto};