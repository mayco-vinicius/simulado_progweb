<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <fieldset>

        <legend>Login</legend>

        <form method="post" action="/login">
            <label for="email">Email</label>
            <input type="email" name="usuario" placeholder="Informe o email" autofocus required>
            <br>

            <label for="senha">Senha</label>
            <input type="password" name="senha" placeholder="Informe a senha" required>
            <br>

            <button type="submit">Entrar</button>
        </form>

    </fieldset>
</body>
</html>
