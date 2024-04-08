<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Compras</title>
</head>
<body>
    <fieldset>
        <legend>Adicionar item</legend>
        <!-- Formulário para adicionar item -->
        <form method="post" action="/adicionar">
            <label for="campo_descricao">Item:</label> <br/>
            <input type="text" name="descricao" id="campo_descricao" placeholder="Informe a descrição do item" required autofocus /><br/>
            <br/>

            <label for="campo_qtde">Quantidade:</label> <br/>
            <input type="number" name="quantidade" id="campo_qtde" placeholder="Quantidade" required min="1" max="100" /><br/>
            <br/>
            
            <label for="campo_solicitante">Solicitante:</label> <br/>
            <select name="solicitante" id="campo_solicitante">
                % for familiar in familiares:
                <option value="{{familiar}}">{{familiar}}</option>
                % end
            </select>
            <br/>
            
            <br/>
            <button type="submit">Adicionar</button>
            <button type="reset">Limpar</button>
        </form>
    </fieldset>
    
    <fieldset>
        <legend>Lista</legend>
        <!-- Link para rota que limpa os itens da lista -->
        <a href="/limpar">Limpar lista</a><br />
        
        <br />
        <!-- Tabela com os itens -->
        <table border="1" width="100%">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Item</th>
                    <th>Qtde</th>
                    <th>Solicitante</th>
                </tr>
            </thead>
            <tbody>
                <!-- Template com condicional verificando se há itens na lista -->
                % if (len(lista_de_compras) == 0):
                    <tr>
                        <!-- Caso a lista esteja vazia irá mostrar msg abaixo -->
                        <td colspan="4" align="center">
                            Nenhum item na lista
                        </td>
                    </tr>
                % else:
                    <!-- Caso tenha itens na lista, irá fazer um loop -->
                    % for i, item in enumerate(lista_de_compras):
                        <!-- Cada item será mostrado -->
                        <tr>
                            <td>{{i+1}}</td>
                            <td>{{item["descricao"]}}</td>
                            <td>{{item["quantidade"]}}</td>
                            <td>{{item["solicitante"]}}</td>
                        </tr>
                    % end
                % end
            </tbody>
        </table>
    </fieldset>
</body>
</html>