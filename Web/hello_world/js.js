document.write("<table border=1>");
for (let i = 1; i<=8; i++){
    document.write("<tr>");
    for (let k = 1; k <=8; k++){
        if (i % 2 == k%2){
            document.write("<td style='font-size: 30px' width=50 height=50 bgcolor=blue align=center >" + "♙" + "</td>");
        }else{
            document.write("<td style='font-size: 30px' width=50 height=50 bgcolor=yellow align=center>" + "♟" + "</td>");
        }
    }
    document.write("</tr>")
}
document.write("</table>")