FROM httpd:2.4

RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install -y gcc 
RUN apt-get install -y make 
RUN apt-get install -y openssl
RUN apt-get install -y libbz2-dev 
RUN apt-get install -y libreadline-dev
RUN apt-get install -y libsqlite3-dev
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"

WORKDIR /usr/local/
RUN git clone git://github.com/yyuu/pyenv.git ./pyenv
RUN mkdir -p ./pyenv/versions ./pyenv/shims

WORKDIR /usr/local/pyenv/plugins/
RUN git clone git://github.com/yyuu/pyenv-virtualenv.git
ENV PYENV_ROOT /usr/local/pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN tee -a /etc/profile.d/pyenv.sh



