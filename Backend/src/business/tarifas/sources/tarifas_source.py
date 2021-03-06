tarifas_sql = '''
    SELECT * FROM 
    (
        SELECT * FROM 
        (
            SELECT * FROM 
            (
                SELECT 
                    FT3_FT4.ID_EMPRESA AS EMPRESA,
                    FT3_FT4.CAR_T1668_ID_MERCADO AS MERCADO,
                    FT3_FT4.CAR_CARG_ANO AS ANO,
                    FT3_FT4.CAR_CARG_PERIODO AS PERIODO,
                    TO_NUMBER(FT3_FT4.CAR_T1668_ESTRATO_SECTOR) AS ESTRATO,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL1_100_OR AS TARIFA1_100,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL1_50_OR AS TARIFA1_50,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL1_00_OR AS TARIFA1_0,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL2 AS TARIFA_2,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL3 AS TARIFA_3,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL4 AS TARIFA_4 
                FROM 
                (
                    (
                        SELECT FT3.* FROM 
                        (
                            SELECT * FROM ENERGIA_CREG_015.CAR_TARIFAS_PUBLICADAS 
                            WHERE 
                                (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                                AND (CAR_T1668_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                                AND CAR_CARG_ANO = :ANIO_ARG 
                                AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS1 
                                AND CAR_T1668_CARGO_HORARIO = 4 
                                AND CAR_T1668_ANIO_CORREGIDO IS NULL
                        ) FT3 
                        LEFT JOIN 
                        (
                            SELECT * FROM ENERGIA_CREG_015.CAR_TARIFAS_PUBLICADAS 
                            WHERE 
                                (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                                AND (CAR_T1668_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                                AND CAR_CARG_ANO = :ANIO_ARG 
                                AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS1 
                                AND CAR_T1668_CARGO_HORARIO = 4 
                                AND CAR_T1668_ANIO_CORREGIDO IS NOT NULL
                        ) FT4 
                        ON FT3.CAR_T1668_ID_MERCADO = FT4.CAR_T1668_ID_MERCADO 
                        AND FT3.ID_EMPRESA = FT4.ID_EMPRESA 
                        AND FT3.CAR_CARG_ANO = FT4.CAR_CARG_ANO 
                        AND FT3.CAR_CARG_PERIODO = FT4.CAR_CARG_PERIODO 
                        WHERE (FT3.CAR_T1668_ANIO_CORREGIDO IS NULL AND FT4.CAR_T1668_ANIO_CORREGIDO IS NULL)
                    )
                    UNION 
                    (
                        SELECT * FROM ENERGIA_CREG_015.CAR_TARIFAS_PUBLICADAS 
                        WHERE 
                            (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                            AND (CAR_T1668_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                            AND CAR_CARG_ANO = :ANIO_ARG 
                            AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS1 
                            AND CAR_T1668_CARGO_HORARIO = 4 
                            AND CAR_T1668_ANIO_CORREGIDO IS NOT NULL
                    )
                ) FT3_FT4
                WHERE FT3_FT4.CAR_T1668_ESTRATO_SECTOR NOT IN (9, 10)
            )
            UNPIVOT (
                (TARIFA)
                FOR NT_PROP
                IN (
                    (TARIFA1_100) AS '1-100', 
                    (TARIFA1_50) AS '1-50',
                    (TARIFA1_0) AS '1-0',
                    (TARIFA_2) AS '2',
                    (TARIFA_3) AS '3',
                    (TARIFA_4) AS '4' 
                )
            )
        )
        PIVOT 
        (
            MAX(TARIFA) 
            FOR 
                ESTRATO 
            IN (1 AS ESTRATO1, 2 AS ESTRATO2, 3 AS ESTRATO3, 4 AS ESTRATO4, 5 AS ESTRATO5, 6 AS ESTRATO6, 7 AS INDUSTRIAL, 8 AS COMERCIAL) 
        )
    ) TARIFAS_MES_ANTERIOR,
    (
        SELECT * FROM 
        (
            SELECT * FROM 
            (
                SELECT 
                    FT3_FT4.ID_EMPRESA AS EMPRESA,
                    FT3_FT4.CAR_T1668_ID_MERCADO AS MERCADO,
                    FT3_FT4.CAR_CARG_ANO AS ANO,
                    FT3_FT4.CAR_CARG_PERIODO AS PERIODO,
                    TO_NUMBER(FT3_FT4.CAR_T1668_ESTRATO_SECTOR) AS ESTRATO,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL1_100_OR AS TARIFA1_100,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL1_50_OR AS TARIFA1_50,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL1_00_OR AS TARIFA1_0,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL2 AS TARIFA_2,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL3 AS TARIFA_3,
                    FT3_FT4.CAR_T1668_TARIFA_NIVEL4 AS TARIFA_4 
                FROM 
                (
                    (
                        SELECT FT3.* FROM 
                        (
                            SELECT * FROM ENERGIA_CREG_015.CAR_TARIFAS_PUBLICADAS 
                            WHERE 
                                (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                                AND (CAR_T1668_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                                AND CAR_CARG_ANO = :ANIO_ARG 
                                AND CAR_CARG_PERIODO = :PERIODO_ARG 
                                AND CAR_T1668_CARGO_HORARIO = 4 
                                AND CAR_T1668_ANIO_CORREGIDO IS NULL
                        ) FT3 
                        LEFT JOIN 
                        (
                            SELECT * FROM ENERGIA_CREG_015.CAR_TARIFAS_PUBLICADAS 
                            WHERE 
                                (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                                AND (CAR_T1668_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                                AND CAR_CARG_ANO = :ANIO_ARG 
                                AND CAR_CARG_PERIODO = :PERIODO_ARG 
                                AND CAR_T1668_CARGO_HORARIO = 4 
                                AND CAR_T1668_ANIO_CORREGIDO IS NOT NULL
                        ) FT4 
                        ON FT3.CAR_T1668_ID_MERCADO = FT4.CAR_T1668_ID_MERCADO 
                        AND FT3.ID_EMPRESA = FT4.ID_EMPRESA 
                        AND FT3.CAR_CARG_ANO = FT4.CAR_CARG_ANO 
                        AND FT3.CAR_CARG_PERIODO = FT4.CAR_CARG_PERIODO 
                        WHERE (FT3.CAR_T1668_ANIO_CORREGIDO IS NULL AND FT4.CAR_T1668_ANIO_CORREGIDO IS NULL)
                    )
                    UNION 
                    (
                        SELECT * FROM ENERGIA_CREG_015.CAR_TARIFAS_PUBLICADAS 
                        WHERE 
                            (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                            AND (CAR_T1668_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                            AND CAR_CARG_ANO = :ANIO_ARG 
                            AND CAR_CARG_PERIODO = :PERIODO_ARG 
                            AND CAR_T1668_CARGO_HORARIO = 4 
                            AND CAR_T1668_ANIO_CORREGIDO IS NOT NULL
                    )
                ) FT3_FT4
                WHERE FT3_FT4.CAR_T1668_ESTRATO_SECTOR NOT IN (9, 10)
            )
            UNPIVOT (
                (TARIFA)
                FOR NT_PROP
                IN (
                    (TARIFA1_100) AS '1-100', 
                    (TARIFA1_50) AS '1-50',
                    (TARIFA1_0) AS '1-0',
                    (TARIFA_2) AS '2',
                    (TARIFA_3) AS '3',
                    (TARIFA_4) AS '4' 
                )
            )
        )
        PIVOT 
        (
            MAX(TARIFA) 
            FOR 
                ESTRATO 
            IN (1 AS ESTRATO1, 2 AS ESTRATO2, 3 AS ESTRATO3, 4 AS ESTRATO4, 5 AS ESTRATO5, 6 AS ESTRATO6, 7 AS INDUSTRIAL, 8 AS COMERCIAL) 
        )
    ) TARIFAS_MES_CONSULTADO,
    (
        SELECT * FROM 
        (
            SELECT * FROM 
            (
                SELECT 
                    FT3_FT4.ID_EMPRESA AS EMPRESA,
                    FT3_FT4.CAR_T1668_ID_MERCADO AS MERCADO,
                    FT3_FT4.CAR_CARG_ANO AS ANO,
                    FT3_FT4.CAR_CARG_PERIODO AS PERIODO,
                    TO_NUMBER(FT3_FT4.CAR_T1668_ESTRATO_SECTOR) AS ESTRATO,
                    CAR_T1668_PORCENTAJE_SUB100_OR AS PORCENTAJE_SUB1_100,
                    CAR_T1668_PORCENTAJE_SUB50_OR AS PORCENTAJE_SUB1_50,
                    CAR_T1668_PORCENTAJE_SUB00_OR AS PORCENTAJE_SUB1_0,
                    0 AS PORCENTAJE_SUB2,
                    0 AS PORCENTAJE_SUB3,
                    0 AS PORCENTAJE_SUB4 
                FROM 
                (
                    (
                        SELECT FT3.* FROM 
                        (
                            SELECT * FROM ENERGIA_CREG_015.CAR_TARIFAS_PUBLICADAS 
                            WHERE 
                                (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                                AND (CAR_T1668_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                                AND CAR_CARG_ANO = :ANIO_ARG 
                                AND CAR_CARG_PERIODO = :PERIODO_ARG 
                                AND CAR_T1668_CARGO_HORARIO = 4 
                                AND CAR_T1668_ANIO_CORREGIDO IS NULL
                        ) FT3 
                        LEFT JOIN 
                        (
                            SELECT * FROM ENERGIA_CREG_015.CAR_TARIFAS_PUBLICADAS 
                            WHERE 
                                (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                                AND (CAR_T1668_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                                AND CAR_CARG_ANO = :ANIO_ARG 
                                AND CAR_CARG_PERIODO = :PERIODO_ARG 
                                AND CAR_T1668_CARGO_HORARIO = 4 
                                AND CAR_T1668_ANIO_CORREGIDO IS NOT NULL
                        ) FT4 
                        ON FT3.CAR_T1668_ID_MERCADO = FT4.CAR_T1668_ID_MERCADO 
                        AND FT3.ID_EMPRESA = FT4.ID_EMPRESA 
                        AND FT3.CAR_CARG_ANO = FT4.CAR_CARG_ANO 
                        AND FT3.CAR_CARG_PERIODO = FT4.CAR_CARG_PERIODO 
                        WHERE (FT3.CAR_T1668_ANIO_CORREGIDO IS NULL AND FT4.CAR_T1668_ANIO_CORREGIDO IS NULL)
                    )
                    UNION 
                    (
                        SELECT * FROM ENERGIA_CREG_015.CAR_TARIFAS_PUBLICADAS 
                        WHERE 
                            (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                            AND (CAR_T1668_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                            AND CAR_CARG_ANO = :ANIO_ARG 
                            AND CAR_CARG_PERIODO = :PERIODO_ARG 
                            AND CAR_T1668_CARGO_HORARIO = 4 
                            AND CAR_T1668_ANIO_CORREGIDO IS NOT NULL
                    )
                ) FT3_FT4
                WHERE FT3_FT4.CAR_T1668_ESTRATO_SECTOR NOT IN (9, 10)
            )
            UNPIVOT (
                (PORCENTAJE_SUB) 
                FOR NT_PROP 
                IN (
                    (PORCENTAJE_SUB1_100) AS '1-100',
                    (PORCENTAJE_SUB1_50) AS '1-50',
                    (PORCENTAJE_SUB1_0) AS '1-0',
                    (PORCENTAJE_SUB2) AS '2',
                    (PORCENTAJE_SUB3) AS '3',
                    (PORCENTAJE_SUB4) AS '4' 
                )
            )
        )
        PIVOT 
        (
            MAX(PORCENTAJE_SUB) 
            FOR 
                ESTRATO 
            IN (1 AS ESTRATO1, 2 AS ESTRATO2, 3 AS ESTRATO3, 4 AS ESTRATO4, 5 AS ESTRATO5, 6 AS ESTRATO6, 7 AS INDUSTRIAL, 8 AS COMERCIAL) 
        )
    ) PORCENTAJE_SUB,
    (
        SELECT 
            DISTINCT ID_MERCADO,
            NOM_MERCADO,
            ESTADO 
        FROM 
            CARG_COMERCIAL_E.MERCADO_EMPRESA 
        WHERE 
            ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG 
            AND NOM_MERCADO NOT LIKE '%Mercado Prueba%' 
            AND NOM_MERCADO NOT LIKE '%Mercado de Prueba%'
    ) MERCADO 
    WHERE 
        TARIFAS_MES_CONSULTADO.MERCADO = TARIFAS_MES_ANTERIOR.MERCADO 
        AND TARIFAS_MES_CONSULTADO.NT_PROP = TARIFAS_MES_ANTERIOR.NT_PROP 
        AND TARIFAS_MES_CONSULTADO.MERCADO = PORCENTAJE_SUB.MERCADO 
        AND TARIFAS_MES_CONSULTADO.NT_PROP = PORCENTAJE_SUB.NT_PROP 
        AND TARIFAS_MES_CONSULTADO.MERCADO = MERCADO.ID_MERCADO 
    ORDER BY TARIFAS_MES_CONSULTADO.MERCADO, TARIFAS_MES_CONSULTADO.NT_PROP
'''
