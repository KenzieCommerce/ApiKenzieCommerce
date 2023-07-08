# ApiKenzieCommerce
Projeto final M5
<br/>
# Doc:
https://kenziecommerce-k4me.onrender.com/api/docs/swagger-ui/
<br/>
# Deploy da aplicação:
https://kenziecommerce-k4me.onrender.com

## Endpoints:
<br/>


| Método | Endpoint                   | Responsabilidade                                  | Autenticação                           |
| ------ | -------------------------- | ------------------------------------------------- | -------------------------------------- |
| POST   | api/users/                     | Criação de usuário                                | Qualquer usuário, não necessita token  |
| GET    | api/users/adm/                    | Lista todos os usuários                           | Apenas Admnistradores                  |
| GET    | api/users/id/    |lista um usuário pelo id |   Apenas dono da conta
| PUT  | api/users/:id/                 | Atualiza um usuário                               | Apenas Admnistradores ou dono da conta |
| PATCH | api/users/:id/ | Atualiza parcialmente informações de  um usuário |  Apenas adm ou  o dono da conta |
| DELETE | api/users/:id/                 |exclui uma conta                 | Apenas Admnistradores ou dono da conta |                 |
| POST   | api/users/login/                     | Gera o token de autenticação                      | Qualquer usuário, não necessita token  |
| PUT   | api/users/cart/id/                | Adiciona um produto ao carrinho                             | Apenas dono da conta                  |
| PATCH    | api/users/cart/id/ | exclui um produto no carrinho                         | apenas o dono da conta |
| GET    |api/users/cart/ |  Lista todos os produtos no carrinho  | apenas o dono da conta  |

<br/>

| Método | Endpoint                   | Responsabilidade                                  | Autenticação                           |
| ------ | -------------------------- | ------------------------------------------------- | -------------------------------------- |
| GET | api/products/                 | Listar todos os produtos                           | Apenas adm e funcionários 
| POST| api/products/                 | Cadastrar um produto                              | Apenas adm e funcionários
| GET|  api/products/id/                | Busca um produto pelo id                                    | Apenas adm e funcionários
|PATCH| api/products/id/                   | Atualiza parcialmente informções de um produto           | Apenas adm e funcionários
|DELETE|api/product/id/                      | Exclui um produto do banco de dados                  | Apenas adm e funcionários

