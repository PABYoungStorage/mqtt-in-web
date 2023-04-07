var ws = new WebSocket('ws://youngstorage.in:15674/ws');
var client = Stomp.over(ws);
const dockerstats = document.getElementById("dockerstats")
const cpu = document.getElementById("cpu")
const Memory_Usage = document.getElementById("Memory_Usage")
const Memory_Percentage = document.getElementById("Memory_Percentage")
const Net_I = document.getElementById("Net_I")
const Block_I = document.getElementById("Block_I")
const PID = document.getElementById("PID")
const badge = document.getElementById("badge")

var on_connect = function () {
    id = client.subscribe('/queue/testwire', function (d) {
        var p = JSON.parse(d.body);
        let dockerstatsKey = ["cpu","Memory_Usage","Memory_Percentage","Net_I","Block_I","PID"]
        Object.keys(p).map(a => {
            switch(a){
                case "connected":{
                    if(p[a] == true){
                        badge.className = "badge success"
                    }else{
                        badge.className = "badge"
                    }
                    break
                }
                case "cpu":{
                    cpu.innerHTML = `${a} : ${p[a]}`
                    break
                }
                case "Memory_Usage":{
                    Memory_Usage.innerHTML = `${a} : ${p[a]}`
                    break
                }
                case "Memory_Percentage":{
                    Memory_Percentage.innerHTML = `${a} : ${p[a]}`
                    break
                }
                case "Net_I":{
                    Net_I.innerHTML = `${a}/O : ${p[a]}`
                    break
                }
                case "Block_I":{
                    Block_I.innerHTML = `${a}/O : ${p[a]}`
                    break
                }
                case "PID":{
                    PID.innerHTML = `${a} : ${p[a]}`
                    break
                }
            }
        })
        // console.log(p)
        // lines.push(p);
        // draw(p, true);
    });
};
var on_error = function () {
    console.log('error');
};
client.connect('anish', 'dotmail123', on_connect, on_error, '/');