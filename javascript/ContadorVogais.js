// minha resolução
var txt = 'São Paulo'
function ContarVogal(t){
    t.tolowercase
    ac = t.normalize("NFKD").replace(/[\u0300-\u036f]/g, '')
    array = ac.split("")
    cont = 0
    for(i in array)
    if (array[i].includes('a')||array[i].includes('e')||array[i].includes('i')||array[i].includes('o')||array[i].includes('u')||array[i].includes('y')){
       cont+=1

    }
return console.log(`A palavra ${t.toUpperCase()} possui ${cont} vógais`)
}
ContarVogal(txt)
//GPT
function contarVogais(str) {
    const vogais = str.match(/[aeiou]/gi);
    return vogais ? vogais.length : 0;
  }
  
  // Exemplo de uso:
  console.log(contarVogais("Olá, mundo!")); // Saída: 4