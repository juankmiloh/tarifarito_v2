componenteP097_sql = '''
    SELECT * FROM 
    (
        SELECT 
            CPTEP.*
        FROM
        (
            SELECT 
                FT9.*,
                CPTE_G.C28_CG AS CG,
                CPTE_T.C5_CT AS CT,
                FT10.*
            FROM
            (
                SELECT 
                    ((LEAST(1,((T9.C1_C7 + T9.C3_C2) / (T10.C12_C4 + T9.C13_C15 + T10.C14_C6 + T9.C15_C16))) * ((C25_C14 * ((T9.C4_C8 + T9.C6_C3) / (T9.C1_C7 + T9.C3_C2))) + (1 - C25_C14) * (T13.C9_C1 + T9.C10_C4))) + ((1 - (LEAST(1,((T9.C1_C7 + T9.C3_C2) / (T10.C12_C4 + T9.C13_C15 + T10.C14_C6 + T9.C15_C16)))) - (T9.C19_C9 + T9.C20_C10)) * (T9.C8_C6 / T9.C7_C5)) + T9.C24_C13 + T9.C26_C11) AS C28_CG 
                FROM
                (
                    SELECT 
                        CAR_T1671_DMRE AS C12_C4,
                        CAR_T1671_PRRE AS C14_C6,
                        CAR_T1671_ECC AS C2_C2,
                        CAR_T1671_VECC AS C5_C3 
                    FROM ENERGIA_CREG_015.CAR_T1671_INFORMACION_ASIC_LAC 
                    WHERE CAR_CARG_ANO = :ANIO_ARG 
                    and CAR_CARG_PERIODO = :PERIODO_ARG 
                    AND (CAR_T1671_ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                ) T10,
                (
                    SELECT 
                        CAR_1672_ECC AS C1_C7,
                        CAR_1672_AECC AS C3_C2,
                        CAR_1672_VECC AS C4_C8,
                        CAR_1672_CB AS C7_C5,
                        CAR_1672_VCB AS C8_C6,
                        CAR_1672_ADMRE_G AS C13_C15,
                        CAR_1672_APRRE_G AS C15_C16,
                        CAR_1672_AVECC AS C6_C3,
                        CAR_1672_AGPE AS C19_C9,
                        CAR_1672_GD AS C20_C10,
                        CAR_1672_AJ AS C24_C13,
                        CAR_1672_ALFA AS C25_C14,
                        CAR_1672_GTR AS C26_C11,
                        CAR_1672_CFNC AS C27_C12,
                        CAR_1672_AMC AS C10_C4,
                        CAR_CARG_ANO,
                        CAR_CARG_PERIODO 
                    FROM 
                        ENERGIA_CREG_015.CAR_VAR_COSTO_UNT_PS_CU_119_UR 
                    WHERE 
                        CAR_CARG_ANO = :ANIO_ARG 
                        AND CAR_CARG_PERIODO = :PERIODO_ARG 
                        AND (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                        AND (CAR_1672_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
                ) T9,
                (
                SELECT 
                    CAR_T1673_MC AS C9_C1 
                FROM ENERGIA_CREG_015.CAR_INFORMACION_GENERAL 
                    WHERE 
                        CAR_CARG_ANO = :ANIO_ARG 
                        AND CAR_CARG_PERIODO = :PERIODO_ARG 
                )T13
            )CPTE_G,
            (
                SELECT CAR_T1673_STN_MO AS C5_CT 
                FROM ENERGIA_CREG_015.CAR_INFORMACION_GENERAL
                WHERE CAR_CARG_ANO = 2020
                AND CAR_CARG_PERIODO = :PERIODO_ARG 
            )CPTE_T,
            (
                SELECT 
                    CAR_T1671_DMRE AS C2_C4,
                    CAR_T1671_PRRE AS C3_C6,
                    CAR_T1671_DMNR AS C4_C5,
                    CAR_T1671_PRNR AS C5_C7
                FROM ENERGIA_CREG_015.CAR_T1671_INFORMACION_ASIC_LAC
                WHERE CAR_CARG_ANO = :ANIO_ARG 
                and CAR_CARG_PERIODO = :PERIODO_ARG 
                AND (CAR_T1671_ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
            )FT10,
            (
                SELECT 
                    CAR_CARG_ANO,
                    CAR_CARG_PERIODO,
                    ID_EMPRESA,
                    CAR_1672_ID_MERCADO,
                    CAR_1672_ADR_IPRSTN AS C6_C17,
                    CAR_1672_APR_IPRSTN AS C7_C18 
                FROM ENERGIA_CREG_015.CAR_VAR_COSTO_UNT_PS_CU_119_UR
                WHERE 
                    CAR_CARG_ANO = :ANIO_ARG 
                    AND CAR_CARG_PERIODO = :PERIODO_ARG 
                    AND (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                    AND (CAR_1672_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG)
            )FT9
        )CPTEP
    )
    WHERE ROWNUM = 1
'''