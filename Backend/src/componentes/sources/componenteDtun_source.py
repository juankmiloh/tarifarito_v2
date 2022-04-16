componenteDtun_sql = '''
    SELECT 
        FT11.*,
        FT12.*,
        C1 - (C2 / 2) AS C3,
        C1 - C2 AS C4 
    FROM 
    (
        SELECT 
            TO_NUMBER(B.CAR_1674_ADD) AS AD,
            B.CAR_1674_DT_UN_NT1 AS C1,
            B.CAR_1674_DT_UN_NT2 AS C5,
            B.CAR_1674_DT_UN_NT3 AS C6 
        FROM ENERGIA_CREG_015.CAR_T1674_INFORMACION_ADD A,
            ENERGIA_CREG_015.CAR_T1674_INFORMACION_ADD B 
        WHERE 
            A.CAR_1674_ADD = B.CAR_1674_ADD 
            AND A.CAR_CARG_ANO = :ANIO_ARG 
            AND A.CAR_CARG_PERIODO = :PERIODO_ARG 
            AND B.CAR_CARG_ANO = :ANIO_ARG 
            AND B.CAR_CARG_PERIODO = :PERIODO_ARG 
    ) FT12,
    (
        SELECT 
            CAR_CARG_ANO,
            CAR_CARG_PERIODO,
            CAR_T1679_ID_EMPRESA,
            CAR_T1679_CDI AS C2,
            CAR_T1679_DT4 AS C7 
        FROM ENERGIA_CREG_015.CAR_INFORMACION_ASIC_LAC_DISTI 
        WHERE 
            CAR_CARG_ANO = :ANIO_ARG 
            AND CAR_CARG_PERIODO = :PERIODO_ARG 
            AND (CAR_T1679_ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG)
    )FT11
'''