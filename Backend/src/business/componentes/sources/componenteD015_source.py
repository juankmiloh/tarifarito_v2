componenteD015_sql = '''
    SELECT 
        CPTE_D.*,
        C14+(C3/(1-C10/100))+C1+C2+C11 AS C18,
        C14+(C3/(1-C10/100))+C2+C11 AS C19,
        C14+(C3/(1-C10/100))+(C1/2)+C2+C11 AS C20,
        C15+C3+C12 AS C21,
        C16+C4+C13 AS C22,
        C17 AS C23,
        :ANIO_ARG AS ANO,
        :PERIODO_ARG AS PERIODO,
        :EMPRESA_ARG AS EMPRESA,
        :MERCADO_ARG AS MERCADO 
    FROM
    (
        SELECT 
            CAR_T1679_DT1 AS DT1,
            CAR_T1679_DT2 AS DT2,
            CAR_T1679_DT3 AS DT3,
            CAR_T1679_DT4 AS DT4,
            FT11.C1, FT11.C2, FT11.C3, FT11.C4,
            FT13.C5,
            FT11.C6, FT11.C7, FT11.C8, FT11.C9,
            FT11.C10, FT11.C11, FT11.C12, FT11.C13,
            C5 / (1 - C6 / 100) AS C14,
            C5 / (1 - C7 / 100) AS C15,
            C5 / (1 - C8 / 100) AS C16,
            C5 / (1 - C9 / 100) AS C17 
        FROM
        (
            SELECT 
                CAR_T1679_CDI AS C1,
                CAR_T1679_CDA AS C2,
                CAR_T1679_CD2 AS C3,
                CAR_T1679_CD3 AS C4,
                CAR_T1679_PR1 AS C6,
                CAR_T1679_PR2 AS C7,
                CAR_T1679_PR3 AS C8,
                CAR_T1679_PR4 AS C9,
                CAR_T1679_P1 AS C10,
                CAR_T1679_DTCS1 AS C11,
                CAR_T1679_DTCS2 AS C12,
                CAR_T1679_DTCS3 AS C13,
                CAR_T1679_DT1,
                CAR_T1679_DT2,
                CAR_T1679_DT3,
                CAR_T1679_DT4 
            FROM ENERGIA_CREG_015.CAR_INFORMACION_ASIC_LAC_DISTI
            WHERE 
                CAR_CARG_ANO = :ANIO_ARG 
                AND CAR_CARG_PERIODO = :PERIODO_ARG 
                AND (CAR_T1679_ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG)
        )FT11,
        (
            SELECT 
                CASE 
                    WHEN :EMPRESA_ARG = 2249 THEN CAR_T1673_CD4_NORTE
                    ELSE CAR_T1673_CD4_CENTRO_SUR
                END AS C5
            FROM ENERGIA_CREG_015.CAR_INFORMACION_GENERAL 
            WHERE 
                CAR_CARG_ANO = :ANIO_ARG 
                AND CAR_CARG_PERIODO = :PERIODO_ARG
        )FT13
    )CPTE_D
'''