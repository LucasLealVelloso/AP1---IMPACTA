# AP1 IMPACTA
(Atividade P1 realizada em sala de aula)
<h3>• Print da execução do Swagger no FastAPI</h3>
<img src='swager.jpeg'>
<h3>• Print do banco com um usuario cadastrado</h3>
<img src='bdusuarios.jpeg'>
<h3>• Print do banco com produtos cadastrados</h3>
<img src='bdprodutos.jpeg'>

# Instalar docker desktop (aqui já tem tudo, abra todos os programas)
  https://www.docker.com/products/docker-desktop/
<br />Instalar python na store do windows 
  <br />Store está no menu ininiar
<br />Instalar dbeaver
  <br />https://dbeaver.io/download/

# comandos api
   <br />cd backend
   <br />python -m venv env
   <br />env\Scripts\activate
   <br />(env)pip install -r requirements-dev.txt
   <br />docker compose up -d
   <br />ver se a conexao funciona no dbeaver

# comandos db
   <br />cd banckend
  <br /> (env)python main.py
   <br />ver se a tabela foi criada no dbeaver
  <br /> testar endpoints no localhost:8003\docs
  
O front usaria isso apos criar os arquivos
cd frontend
npm install
npm run start
ir para http://localhost:3000

exemplos de conexões
# postgree modo 1
engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")

# postgree modo 2 psycopg2
engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/mydatabase")

# mysql
engine = create_engine("mysql://scott:tiger@localhost/foo")
")
# sql server
engine = create_engine("mssql+pymssql://scott:tiger@hostname:port/dbname")
