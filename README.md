# ApiKenzieCommerce
Projeto final M5
####  Api para gerenciamento de e-commerce utilizando Django restframework 



# Doc:
https://kenziecommerce-k4me.onrender.com/api/docs/swagger-ui/



# Deploy da aplicação:
https://kenziecommerce-k4me.onrender.com


### Features

- [x] Cadastro de usuário comum ou funcionário
- [x] Cadastro e listagem de produtos
- [x] Listagem de pedidos
- [x] Carrinho de compras adição e remoção de produtos
- [ ] Criação de superusuário (admin) (criação via terminal)
## Endpoints:
<br/>

### Obs. Usuários Administradores tem acesso a todas as rotas

| Método | Endpoint                   | Responsabilidade                                  | Autenticação                           |
| ------ | -------------------------- | ------------------------------------------------- | -------------------------------------- |
| POST   | api/users/                     | Criação de usuário                                | Qualquer usuário, não necessita token  |
| GET    | api/users/adm/                    | Lista todos os usuários                           | Apenas Administradores                  |
| GET    | api/users/:id/    |lista um usuário pelo id                                      |   Apenas dono da conta 
| PUT  | api/users/:id/                 | Atualiza um usuário                               | Apenas o dono da conta |
| PATCH | api/users/:id/ | Atualiza parcialmente informações de  um usuário |  Apenas o dono da conta |
| DELETE | api/users/:id/                 |exclui uma conta                                   | Apenas a dono da conta |                 |
| POST   | api/users/login/                     | Gera o token de autenticação                      | Qualquer usuário, não necessita token  |
| PUT   | api/users/cart/:id/                | Adiciona um produto ao carrinho                             | Apenas dono da conta                  |
| PATCH    | api/users/cart/:id/ | exclui um produto no carrinho                         | Apenas o dono da conta |
| GET    |api/users/cart/ |  Lista todos os produtos no carrinho  | Apenas o dono da conta  |

<br/>

| Método | Endpoint                   | Responsabilidade                                  | Autenticação                           |
| ------ | -------------------------- | ------------------------------------------------- | -------------------------------------- |
| GET | api/products/                 | Listar todos os produtos                           | Qualquer usuário 
| POST| api/products/                 | Cadastrar um produto                              | Apenas funcionários
| GET|  api/products/:id/                | Busca um produto pelo id                                    | Qualquer usuário
|PATCH| api/products/:id/                   | Atualiza parcialmente informções de um produto           | Apenas funcionários
|DELETE|api/product/:id/                      | Exclui um produto do banco de dados                  | Apenas funcionários

<br/>

| Método | Endpoint                   | Responsabilidade                                  | Autenticação                           |
| ------ | -------------------------- | ------------------------------------------------- | -------------------------------------- |
|GET | api/orders/                     |  Lista todos os pedidos do site                         | Apenas adm |
|GET |  api/orders/:id/                | Busca um pedido específico pelo id                                | Apenas o dono da conta |
|POST | api/orders/                    | Cria um pedido                                                        | Usuário logado  |
|PATCH | api/orders/:id/                    | Atualiza o pedido                                                  | apenas vendedor |


