--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Aluguel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Aluguel" (
    "ID_Aluguel" integer NOT NULL,
    "ID_Cliente" integer,
    "ID_Carro" integer,
    "Data_Aluguel" date NOT NULL,
    "Data_Devolucao" date NOT NULL,
    "Local_LugCar" character varying(150),
    "Valor_Total" money
);


ALTER TABLE public."Aluguel" OWNER TO postgres;

--
-- Name: Aluguel_ID_Aluguel_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Aluguel" ALTER COLUMN "ID_Aluguel" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Aluguel_ID_Aluguel_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Carros; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Carros" (
    "ID_Carro" integer NOT NULL,
    "Placa_Carro" character(7) NOT NULL,
    "Modelo_Carro" character varying(100) NOT NULL,
    "Descricao_Carro" character varying(255),
    "Fabricante_Carro" character varying(100) NOT NULL,
    "Ano_Carro" integer NOT NULL,
    "Diaria_Carro" money NOT NULL
);


ALTER TABLE public."Carros" OWNER TO postgres;

--
-- Name: Carros_ID_Carro_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Carros" ALTER COLUMN "ID_Carro" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Carros_ID_Carro_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Clientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Clientes" (
    "ID_Cliente" integer NOT NULL,
    "Nome_Cliente" character varying(255) NOT NULL,
    "Cpf_Cliente" character(11) NOT NULL,
    "Telefone_Cliente" character(11),
    "Endereco_Cliente" character varying(100) NOT NULL,
    "Data_Nascimento" date
);


ALTER TABLE public."Clientes" OWNER TO postgres;

--
-- Name: Clientes_ID_Cliente_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Clientes" ALTER COLUMN "ID_Cliente" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Clientes_ID_Cliente_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: Aluguel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Aluguel" ("ID_Aluguel", "ID_Cliente", "ID_Carro", "Data_Aluguel", "Data_Devolucao", "Local_LugCar", "Valor_Total") FROM stdin;
1	4	3	2023-02-27	2023-02-28	BR222 km6 8000	\N
\.


--
-- Data for Name: Carros; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Carros" ("ID_Carro", "Placa_Carro", "Modelo_Carro", "Descricao_Carro", "Fabricante_Carro", "Ano_Carro", "Diaria_Carro") FROM stdin;
1	GHM0248	Peugeot 208	cor cinza, quatro portas, motor 1.0	Peugeot	2020	R$ 100,00
2	FOR2640	Voyage	cor branco,quatro portas,motor 1.0	Volkswagen	2019	R$ 110,00
3	JMC2418	Fiat Cronos	cor preta,quatro portas,motor 1.3	Fiat	2022	R$ 118,00
4	POV1256	Renault Kwid	cor azul, quatro portas, motor 1.0	Renault	2021	R$ 97,00
5	ZRT8956	Fiat Argo	cor preta, quatro portas, motor 1.3	Fiat	2023	R$ 120,00
6	YKL1478	Gol	cor branco, quatro portas, motor 1.0	Volkswagen	2020	R$ 98,00
8	SAF1222	Fiat Mobi	cor vermelho,quatro portas,motor 1.0	Fiat	2022	R$ 97,00
9	TRV4597	Chevrolet Onix	cor prata, quatro portas, motor 1.3	Chevrolet	2023	R$ 114,00
10	BJM4758	Hyundai HB20	cor prata,quatro portas,motor 1.0	Hyundai	2022	R$ 110,00
\.


--
-- Data for Name: Clientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Clientes" ("ID_Cliente", "Nome_Cliente", "Cpf_Cliente", "Telefone_Cliente", "Endereco_Cliente", "Data_Nascimento") FROM stdin;
1	Ana Pires	12336978925	85923456987	Rua Napoli 37	1885-05-15
2	Filipe Castro	14523678996	85932561478	Rua Acarau 36 -Potira-Caucaia-CE	1890-02-05
3	Ana Luiza	45678936921	85916123547	Rua Costa Mendes 47 -Fortaleza-CE	1887-08-20
4	Emanuel Gomes	78965412325	85912457896	Rua Costa Barros 16 -Ant.Bezerra-Fortaleza-CE	1979-09-25
5	Vitor Pereira	36985214789	85963251479	Rua Solinge 47 -Parq.Albano-Jurema-Caucaia-CE	1984-11-27
\.


--
-- Name: Aluguel_ID_Aluguel_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Aluguel_ID_Aluguel_seq"', 2, true);


--
-- Name: Carros_ID_Carro_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Carros_ID_Carro_seq"', 10, true);


--
-- Name: Clientes_ID_Cliente_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Clientes_ID_Cliente_seq"', 6, true);


--
-- Name: Aluguel Aluguel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT "Aluguel_pkey" PRIMARY KEY ("ID_Aluguel");


--
-- Name: Carros Carros_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Carros"
    ADD CONSTRAINT "Carros_pkey" PRIMARY KEY ("ID_Carro");


--
-- Name: Clientes Clientes_Cpf_Cliente_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Clientes"
    ADD CONSTRAINT "Clientes_Cpf_Cliente_key" UNIQUE ("Cpf_Cliente");


--
-- Name: Clientes Clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Clientes"
    ADD CONSTRAINT "Clientes_pkey" PRIMARY KEY ("ID_Cliente");


--
-- Name: Aluguel fk_carro; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT fk_carro FOREIGN KEY ("ID_Carro") REFERENCES public."Carros"("ID_Carro") ON DELETE SET NULL;


--
-- Name: Aluguel fk_cliente; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Aluguel"
    ADD CONSTRAINT fk_cliente FOREIGN KEY ("ID_Cliente") REFERENCES public."Clientes"("ID_Cliente") ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

