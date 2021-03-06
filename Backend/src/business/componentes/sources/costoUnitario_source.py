costoUnitario_sql = '''
    SELECT * FROM 
    (
        (
            SELECT FT7.* FROM 
            (
                SELECT * FROM ENERGIA_CREG_015.CAR_COSTO_UNITARIO_119_UR 
                WHERE 
                    (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                    AND (CAR_T1669_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                    AND CAR_CARG_ANO = :ANIO_ARG 
                    AND CAR_CARG_PERIODO = :PERIODO_ARG 
                    AND CAR_T1676_ANIO_CORREG IS NULL
            )FT7 
            LEFT JOIN 
            (
                SELECT * FROM ENERGIA_CREG_015.CAR_COSTO_UNITARIO_119_UR 
                WHERE 
                    (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                    AND (CAR_T1669_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                    AND CAR_CARG_ANO = :ANIO_ARG 
                    AND CAR_CARG_PERIODO = :PERIODO_ARG 
                    AND CAR_T1676_ANIO_CORREG IS NOT NULL
            )F8 
            ON FT7.CAR_T1669_ID_MERCADO = F8.CAR_T1669_ID_MERCADO 
            AND FT7.ID_EMPRESA = F8.ID_EMPRESA 
            AND FT7.CAR_T1669_NT_PROP = F8.CAR_T1669_NT_PROP 
            AND FT7.CAR_CARG_ANO = F8.CAR_CARG_ANO 
            AND FT7.CAR_CARG_PERIODO = F8.CAR_CARG_PERIODO 
            WHERE (FT7.CAR_T1676_ANIO_CORREG IS NULL AND F8.CAR_T1676_ANIO_CORREG IS NULL) 
        )
        UNION 
        (
            SELECT * FROM ENERGIA_CREG_015.CAR_COSTO_UNITARIO_119_UR 
            WHERE 
                (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                AND (CAR_T1669_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                AND CAR_CARG_ANO = :ANIO_ARG 
                AND CAR_CARG_PERIODO = :PERIODO_ARG 
                AND CAR_T1676_ANIO_CORREG IS NOT NULL
        )
    ) FT7_FT8,
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
    WHERE FT7_FT8.CAR_T1669_ID_MERCADO = MERCADO.ID_MERCADO 
    ORDER BY CAR_T1669_ID_MERCADO, CAR_T1669_NT_PROP
'''