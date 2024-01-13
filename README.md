# Myfirstapp
First we will build our application with the below command.
"docker build -t your-dockerhub-username/calculator-app:latest . "
After buildings we will authenticate our docker hub account.
"docker login"
Now we will push our image to docker hub by below command
" docker push your-dockerhub-username/calculator-app:latest(same name as above)"
