let a = [1,2,3];
for (let i = 0; i<=2; i++){
    a[a.length] = prompt("введи строку");
}
a.sort();
for(v in a){
    
    document.write(v+ ":" + a[v] + "<br>");

    
}
// alert(a);