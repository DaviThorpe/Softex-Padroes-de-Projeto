/* Crie uma fábrica de veículos utilizando o padrão Prototype com base no exemplo apresentado no Hipertexto 2. Os requisitos do projeto devem ser:

- implemente uma classe abstrata Veículo com um construtor padrão e os métodos clone e represent;
- o construtor da classe Veículo deve receber modelo, marca, cor e numeroRodas como parâmetros;
- crie pelo menos duas subclasses da classe Veículo, que acrescentem um ou mais atributos, por exemplo: carro que tem dois campos a mais, como numeroRodas e numeroPortas;
- desenvolva uma classe Aplicação que deve criar um array com seis veículos com dois tipos de veículos diferentes (subclasses), utilizando o método clone dos objetos para preencher o array;
- na classe Aplicação, implemente um método que retorne um array com o mesmo tamanho do array de veículos, onde cada elemento deve ser um clone dos elementos do array veículos;
- no final, deve imprimir na tela o retorno da função represent de cada elemento desse novo array de clones de veículos. */


const Veiculo = class {
    constructor(modelo, marca, cor, numeroRodas){
        this.modelo = modelo;
        this.marca = marca;
        this.cor = cor;
        this.numeroRodas = numeroRodas;
    };
    clone(obj){ 
        obj.__proto__;
    };

    represent(){
        console.log(`Modelo: ${this.modelo}, Marca: ${this.marca}, Cor: ${this.cor}, Rodas: ${this.rodas}`); 
    };
};

const carro = class extends Veiculo{
    constructor(modelo, marca, cor, numeroRodas, numeroDePortas){
        super(modelo, marca, cor, numeroRodas);
        this.numeroDePortas = numeroDePortas;
        

        let cloneCarro = {
            modelo: this.modelo,
            marca: this.marca,
            cor: this.cor,
            numeroRodas: this.numeroRodas,
            numeroDePortas: this.numeroDePortas
        }
        Veiculo.prototype.clone=function(obj){
            obj.prototype = cloneCarro;
        }
            Veiculo.prototype.represent=function(){
                console.log(`Modelo: ${this.modelo}, Marca: ${this.marca}, Cor: ${this.cor}, Rodas: ${this.numeroRodas}, Portas: ${this.numeroDePortas}`);
            };
    };
};

const aviao = class extends Veiculo {
    constructor(modelo, marca, cor, numeroRodas, turbinas){
        super(modelo, marca, cor, numeroRodas);
        this.turbinas = turbinas;

        let cloneMoto = {
            modelo: this.modelo,
            marca: this.marca,
            cor: this.cor,
            numeroRodas: this.numeroRodas,
            turbinas: this.turbinas
        }
        Veiculo.prototype.clone=function(obj){
            return obj.prototype = cloneMoto;
        }
            Veiculo.prototype.represent=function(){
                console.log(`Modelo: ${this.modelo}, Marca: ${this.marca}, Cor: ${this.cor}, Rodas: ${this.numeroRodas}, Turbinas ${this.turbinas}`);
            };
    };
};

// Criando a Array 'veiculos'
    
const veiculos = [];

// Criando os objetos da classe Carros:

var AstonVulcan = new carro('Vulcan 2015', 'Aston Martin', 'Preto', 4, 4);
AstonVulcan.represent();
AstonVulcan.clone(AstonVulcan);

var AstonV12 = new carro('V12 Vantage Gr.3', 'Aston Martin', 'Amarelo', 4, 4);
AstonV12.represent();
AstonV12.clone(AstonV12);

var AstonDB3S = new carro('DB3S CN.1 1953', 'Aston Martin', 'Verde', 4, 4);
AstonDB3S.represent();
AstonDB3S.clone(AstonDB3S);

// Criando os objetos da classe Avioes:

var Boeing = new aviao('Boeing 274', 'Boeing', 'Branco', 8, 4);
Boeing.represent();
Boeing.clone(Boeing);

var BoeingStrat = new aviao("Boeing 307 Stratoliner", 'Boeing', 'Branco', 8, 4);
BoeingStrat.represent();
BoeingStrat.clone(BoeingStrat);

var Airbus = new aviao('Airbus 380', 'Airbus', 'Branco', 8, 4);
Airbus.represent();
Airbus.clone(Airbus);

// Inserindo os obejetos dentro do Array 'veiculos'

veiculos.push(AstonVulcan);
veiculos.push(AstonV12);
veiculos.push(AstonDB3S);

veiculos.push(Boeing);
veiculos.push(BoeingStrat);
veiculos.push(Airbus);

console.log(veiculos);
