DROP TABLE IF EXISTS public."Workout";
DROP TABLE IF EXISTS public."Circuit";
DROP TABLE IF EXISTS public."Food";
DROP TABLE IF EXISTS public."Appointment";
DROP TABLE IF EXISTS public."Personal";
DROP TABLE IF EXISTS public."Manager";
DROP TABLE IF EXISTS public."Client";
DROP TABLE IF EXISTS public."User";


CREATE TABLE IF NOT EXISTS public."User"
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 10 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    password character varying(255) COLLATE pg_catalog."default" NOT NULL,
    kind character(1) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "User_pkey" PRIMARY KEY (id),
    CONSTRAINT "User_email_key" UNIQUE (email)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."User"
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public."Client"
(
    id integer NOT NULL,
    "weight (Kg)" integer NOT NULL,
    "height (cm)" integer NOT NULL,
    sex character(1) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Client_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Client"
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public."Manager"
(
    id integer NOT NULL,
    CONSTRAINT "Manager_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Manager"
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public."Personal"
(
    id integer NOT NULL,
    manager_id integer NOT NULL,
    CONSTRAINT "Personal_pkey" PRIMARY KEY (id),
    CONSTRAINT manager FOREIGN KEY (manager_id)
        REFERENCES public."Manager" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Personal"
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public."Appointment"
(
    id integer NOT NULL,
    client_id integer NOT NULL,
    date date NOT NULL,
    personal_id integer,
    "time" time with time zone NOT NULL,
    CONSTRAINT "Appointment_pkey" PRIMARY KEY (id),
    CONSTRAINT client FOREIGN KEY (client_id)
        REFERENCES public."Client" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT personal FOREIGN KEY (personal_id)
        REFERENCES public."Personal" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Appointment"
    OWNER to postgres;


CREATE TABLE IF NOT EXISTS public."Circuit"
(
    id integer NOT NULL,
    client_id integer NOT NULL,
    day integer NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    repetitions integer NOT NULL,
    CONSTRAINT "Circuit_pkey" PRIMARY KEY (id),
    CONSTRAINT client FOREIGN KEY (client_id)
        REFERENCES public."Client" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Circuit"
    OWNER to postgres;



CREATE TABLE IF NOT EXISTS public."Food"
(
    id integer NOT NULL,
    client_id integer NOT NULL,
    day integer NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    "quantity (g)" integer NOT NULL,
    "energy (cal)" integer NOT NULL,
    CONSTRAINT "Food_pkey" PRIMARY KEY (id),
    CONSTRAINT id FOREIGN KEY (client_id)
        REFERENCES public."Client" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Food"
    OWNER to postgres;



CREATE TABLE IF NOT EXISTS public."Workout"
(
    id integer NOT NULL,
    circuit_id integer NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    repetitions integer NOT NULL,
    duration interval NOT NULL,
    CONSTRAINT "Workout_pkey" PRIMARY KEY (id),
    CONSTRAINT circuit FOREIGN KEY (circuit_id)
        REFERENCES public."Circuit" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Workout"
    OWNER to postgres;