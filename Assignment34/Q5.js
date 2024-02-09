// 5. Write a code which can give grades to students according to theirs scores:
// a. 80-100, A
// b. 70-89, B

// Untitled 2

// c. 60-69, C
// d. 50-59, D
// e. 0-49, F
let result="Z";
switch(result)
{
    case 'A':
            {
                console.log("80-100");
                break;
            }
    case 'B':
            {
                console.log("70-89");
                break;
            }
    case 'C':
            {
                console.log(`60-69`);
                break;
            }
     case 'D':
             {
                console.log(`50-59`);
                break;
             }
     case 'F':
             {
                console.log(`0-49`);
                break;
             }
      default:
              {
                  console.log(`you falild`);
              }

}
