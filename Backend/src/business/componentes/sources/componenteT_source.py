componenteT_sql = '''
        SELECT 
            FT78.ID_EMPRESA,
            FT78.CAR_T1669_ID_MERCADO,
            FT78.CAR_T1669_NT_PROP,
            FT78.CAR_CARG_ANO,
            FT78.CAR_CARG_PERIODO,
            FT78.CAR_T1669_TM AS C3_C6,
            FT13.* 
        FROM 
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
        )FT78,
        (
            SELECT CAR_T1673_STN_MO AS C4_C2 
            FROM ENERGIA_CREG_015.CAR_INFORMACION_GENERAL 
            WHERE CAR_CARG_ANO = :ANIO_ARG 
            AND CAR_CARG_PERIODO = :PERIODO_ARG
        )FT13 
        WHERE FT78.CAR_T1669_NT_PROP = :NTPROP_ARG OR 'TODOS' = :NTPROP_ARG
'''