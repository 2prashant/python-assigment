// 7. Create a human readable time format using the Date time object
// a. YYYY-MM-DD HH:mm
// b. DD-MM-YYYY HH:mm
// c. DD/MM/YYYY HH:mm

let time=new Date();
console.log(`
        time : ${time.toString()}
        time : ${time.getFullYear()}-${time.getMonth()}-${time.getDate()}  ${time.getHours()}:${time.getMinutes()}
        time : ${time.getDay()}-${time.getMonth()}-${time.getFullYear()} ${time.getHours()}:${time.getMinutes()}
        time : ${time.getDay()}/${time.getMonth()}/${time.getFullYear()}  ${time.getHours()}:${time.getMinutes()}
`);