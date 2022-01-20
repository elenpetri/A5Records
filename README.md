 # Portfolio

## :woman_student: Discente:  Élen Fernanda dos Santos Petri
* RA: 1461392121019
* Turma: 1º Semestre - DSM

# Objetivo
Desenvolvimento de um sistema para Internet que sirva como uma página pessoal onde possam ser encontradas as seguintes informações:
 1. Dados do proprietário do sistema (autor da página/aplicação web); <br/>
    a. Uma foto que contenha efeitos de redimensionamento e filtro;
    <br/>
    b. Informações educacionais;
    <br/>
    c. Outras informações pertinentes (interesses, etc.). 
  2. Portfólio (trabalhos desenvolvidos ou que pretende desenvolver); 
  3. Outras informações relevantes ou de interesse do autor/proprietário. 

# Requisitos
* Responsividade de maneira a manter um layout amigável e bem estruturado tanto em um computador de mesa (desktop, laptop e similares) como em um dispositivo móvel;
* Boas  práticas  de  arquitetura  de  informação  na  construção  das interfaces;
* Possuir no mínimo, três interfaces acessíveis a partir de algum mecanismo de navegação;
* Possuir um esquema de cores e layout único com relação aos demais sistemas desenvolvidos  pelos  seus  colegas  de  turma;
* Fazer  uso  de  arquivo  de  fonte  externa,  disponibilizado  pelo  servidor  da aplicação, sendo que a tipografia deve ser adequada à natureza do uso escolhido;
* Conter ao menos uma imagem ou logotipo que seja único e que contribua para dar uma identidade visual ao mesmo;
*  Deve  aplicar  a  tecnologia/conceito  de utilização  de  arquivos  de  imagens responsivas. 

## Restrições de Tecnologia
* O sistema deverá ser desenvolvido utilizando-se CSS 3, com no mínimo 5 regras criadas sem a utilização de frameworks. 
* Fazer uso de pelo menos um framework de CSS 3 para estilizar a aplicação. 
* Desenvolvimento do back end utilizando Python 3. 
* O front end do sistema poderá fazer uso de JavaScript. 
* Implantação do sistema em um servidor de aplicação, tal como Heroku. 

# Arquivos e documentos
* [doc](/doc): pasta que contém documento em PDF com wireframe desktop e mobile;
  * [wireframe](doc/wireframe_desktop_e_mobile.pdf): wireframe desktop e mobile que constitui essencialmente desenhos, com um esquema único de layout, cores e arquitetura da informação coerentes com o projeto;
* [src](/src): pasta que contém o código fonte;
* [src/static](/src/static): pasta que contém a estilização da página (arquivo css), fontes e imagens;
* [src/static/css](/src/static/css): pasta que contém a estilização da página (arquivo css);
  * [body](src/static/css/body.css): arquivo css que contém a estilização do corpo(body) do protótipo;
  * [cores](src/static/css/cores.css): arquivo css que contém a padronização do esquema de cores do protótipo;
  * [header_footer](/src/static/css/header_footer.css): arquivo css que contém a estilização do cabeçalho(header) e do rodapé(footer) do protótipo;
  * [bootstrap](/src/static/css/bootstrap): arquivo que contém biblioteca do framework Bootstrap;
* [src/static/fontes](/src/static/fontes): pasta que contém fonte externa que está sendo utilizada na assinatura da autora no footer;
  * [fontes](/src/static/fontes/Rustling%20Sound.ttf): arquivo de fonte externa que está sendo utilizada na assinatura da autora no footer do protótipo;
* [src/static/imagens](/src/static/imagens): pasta que contém imagens que estão sendo utilizadas no sistema;
  * [icon](/src/static/imagens/icon.png): arquivo utilizado como ícone da aba do navegador;
  * [imagem_autora_1](/src/static/imagens/imagem_autora_1.png): foto da autora exibida na página inicial;
  * [imagem_autora_2](/src/static/imagens/imagem_autora_2.png): foto da autora exibida na página sobre;
  * [logo](/src/static/imagens/logo.png): logo criado como identidade visual, se encontra localizado no header do protótipo;
  * [projeto1](/src/static/imagens/projeto1.png): imagem do projeto 1 exibida na página de projetos;
  * [projeto2](/src/static/imagens/projeto2.png): imagem fictícia dpara demonstrar como será disponibilizado a imagem do projeto 2;
* [src/templates](/src/templates): arquivo que contém os arquivos html (index.html, projetos.html e sobre.html);
  * [index](/src/templates/index.html): arquivo que contém a estruturação em HTML da página inicial do protótipo;
  * [projetos](/src/templates/projetos.html): arquivo que contém a estruturação em HTML da página de projetos do protótipo;
  * [sobre](/src/templates/sobre.html): arquivo que contém a estruturação em HTML da página sobre do protótipo.
* [src/app.py](/src/app.py): arquivo de aplicação que contém o mapeamento de rotas e templetes do site;

## Links para os vídeos no youtube
| [Primeira entrega](https://youtu.be/jT8Ad46LVV8)

| [Segunda entrega](https://youtu.be/uZqqx1TmkWo)

## Passo a passo para a execução do sistema

Clonar o repositório:
```bash
git clone https://github.com/elenpetri/Portifolio.git
```

Criar ambiente virtual Python:
```bash
python -m venv env
```
Iniciar ambiente virtual:

Para Windows:
```bash
.\env\Scripts\activate
```

Para Linux:
```bash
source env/bin/activate
```

Instalar dependências:
```bash
pip install -r requirements.txt
```

Executar aplicação (na pasta src/):
```bash
python app.py
```
### Acesse a aplicação: https://elen-petri.herokuapp.com/

[Voltar ao topo &#8593;](README.md) 
