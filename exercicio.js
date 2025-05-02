// minha resolução
var nome = 'pao com arroz'
function palindrome(n) {
    n = n.replace(/\s+/g, '')
    n = n.toLowerCase()
    ini = 1
    for (ini; n.length >= ini; ini += 1) {
        if (n.substr(ini - 1, 1) != n.substr(-ini, 1)) {
            return console.log('não e um palindrome')
        }
        else if (ini == n.length && n.substr(ini - 1, 1) == n.substr(-ini, 1)) {
            console.log('é um palindrome')
        }
    }
}
//minha resolução
//GPT
function ehPalindromo(str) {
    // Remove espaços e converte tudo para minúsculas
    const limpa = str.toLowerCase().replace(/\s+/g, '');
    // Inverte a string
    const invertida = limpa.split('').reverse().join('');//.split transforma cada caracter em uma array, .reverse reverte essa array, .join soma a array com o caracter que esta dentro da função
    // Compara a original com a invertida
    return limpa === invertida;
}