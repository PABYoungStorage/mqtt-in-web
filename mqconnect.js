var ws = new WebSocket('ws://localhost:15675/ws');
var client = Stomp.over(ws);
const rx = document.getElementById("rx")
const tx = document.getElementById("tx")
const badge = document.getElementById("badge")

var on_connect = function () {
    id = client.subscribe('/queue/9652c9a480a8eth0', function (d) {
        var p = JSON.parse(d.body);

        Object.keys(p).map(a => {
            if (a == "tx") {
                tx.innerHTML = String(p.tx).slice(1, -2)
            }
            else if (a == "rx") {
                rx.innerHTML = String(p.rx).slice(1, -2)
            }
            else if(a == "connected"){
                if(p[a] == true){
                    badge.className = "badge success"
                }else{
                    badge.className = "badge"
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