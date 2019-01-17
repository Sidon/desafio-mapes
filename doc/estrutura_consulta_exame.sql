

DROP TABLE IF EXISTS consulta CASCADE;
CREATE TABLE consulta
(
  numero_guia_consulta integer,
  cod_medico integer not null,
  nome_medico VARCHAR,
  data_consulta DATE,
  valor_consulta NUMERIC,
  CONSTRAINT consulta_pkey PRIMARY KEY (numero_guia_consulta)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE consulta OWNER TO postgres;

DROP TABLE IF EXISTS exame;
CREATE TABLE exame
(
  cod_exame integer,
  numero_guia_consulta integer,
  valor_exame NUMERIC,
  CONSTRAINT exame_pkey PRIMARY KEY (cod_exame,numero_guia_consulta),
  CONSTRAINT numero_guia_consulta_fkey FOREIGN KEY (numero_guia_consulta) REFERENCES CONSULTA (numero_guia_consulta)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE exame OWNER TO postgres;