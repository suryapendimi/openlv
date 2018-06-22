# INSTRUCTIONS:
# to build image: docker build -t sanjeev:rscript .
# to run image and enter shell: docker run -it --rm sanjeev:rscript
# once in container shell, run script: Rscript RPredictionFeederVoltage.R

FROM r-base:3.5.0

RUN apt-get update && apt-get install -y \
r-cran-rmysql

COPY . /app

WORKDIR /app

RUN Rscript install_pkgs.R

CMD [ "bash" ]

#CMD [ "Rscript", "RPredictionFeederVoltage.R"]





