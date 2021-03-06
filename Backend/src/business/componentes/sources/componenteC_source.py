componenteC_sql = '''
        SELECT * FROM 
        (
            SELECT 
                TO_CHAR(FT3.ID_EMPRESA), TO_CHAR(FT3.CAR_T1668_ID_MERCADO), TO_CHAR(FT3.CAR_CARG_ANO), TO_CHAR(FT3.CAR_CARG_PERIODO), FT3.C6, T9.C1, FT7.C7, FT7.C8, FT7.C9, FT7.C10, FT7.C11, T9.C13, NVL(FTC2.C20, 0) AS C20, NVL(FTC2.C22, 0) AS C22, NVL(FTC2.C24, 0) AS C24, NVL(FTC2.C21, 0) AS C21, T9.C14, T9.C15, T9.C16, NVL(FTC2.C23, 0) AS C23, NVL(FTC2.C25, 0) AS C25, T9.C28, T9.C29, T9.C30,
                T9.C31, T9.C32, T9.C36, T9.C34, T9.C33, T9.C37, T9.C35, T9.C38, NVL(FTC2.C59, 0) AS C59, NVL(FT2.C69, 0) AS C69, NVL(FT2.C70, 0) AS C70, NVL(FT2.C71, 0) AS C71, T9.C58, NVL(FTC2.C60, 0) AS C60, T9.C44, T9.C47, T9.C48, NVL(FTC2.C55, 0) AS C55, NVL(FT2.C56, 0) AS C56 
            FROM 
            (
                SELECT 
                    CAR_T1669_ID_MERCADO,
                    CAR_T1669_GM AS C7,
                    CAR_T1669_TM AS C8,
                    CAR_T1669_PRNM AS C9,
                    CAR_T1669_DNM AS C10,
                    CAR_T1669_RM AS C11 
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
                ) FT7_FT8
                WHERE CAR_T1669_NT_PROP = '1-100'
            ) FT7
            LEFT JOIN 
            (
                SELECT ID_EMPRESA, CAR_T1668_ID_MERCADO, CAR_CARG_ANO, CAR_CARG_PERIODO, CAR_T1668_TARIFA_CFJM AS C6 FROM 
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
                            AND CAR_T1668_ANIO_CORREGIDO IS NOT NULL
                    )
                ) FT3_FT4 
                GROUP BY ID_EMPRESA, CAR_T1668_ID_MERCADO, CAR_CARG_ANO, CAR_CARG_PERIODO, CAR_T1668_TARIFA_CFJM
            )FT3 
            ON FT7.CAR_T1669_ID_MERCADO = FT3.CAR_T1668_ID_MERCADO 
            LEFT JOIN 
            (
                SELECT 
                    CAR_1672_CFJ AS C1,
                    CAR_1672_RCT AS C13,
                    CAR_1672_RCAE AS C14,
                    CAR_1672_IFSSRI AS C15,
                    CAR_1672_IFOES AS C16,
                    CASE WHEN CAR_1672_BALANCE_SUBSIDIOS = 'D' THEN 'DEFICITARIO' ELSE 'SUPERAVITARIO' END AS C28,
                    CAR_1672_ANIO AS C29,
                    CAR_1672_TRIM AS C30,
                    CAR_1672_MG_TRIM AS C31,
                    CAR_1672_SUB1 AS C32,
                    CAR_1672_R1 AS C36,
                    CAR_1672_N AS C34,
                    CAR_1672_SUB2 AS C33,
                    CAR_1672_R2 AS C37,
                    CAR_1672_M AS C35,
                    CAR_1672_FACTURACION AS C38,
                    CAR_1672_PUI AS C58,
                    CAR_1672_CREG AS C47,
                    CAR_1672_SSPD AS C48,
                    CASE WHEN CAR_1672_ACTIVIDAD = 'CP' THEN 'COMERCIALIZADOR PURO' ELSE 'COMERCIALIZADOR INTEGRADO' END AS C44,
                    CAR_CARG_ANO,
                    CAR_CARG_PERIODO,
                    ID_EMPRESA,
                    CAR_1672_ID_MERCADO 
                FROM 
                    ENERGIA_CREG_015.CAR_VAR_COSTO_UNT_PS_CU_119_UR 
                WHERE 
                    CAR_CARG_ANO = :ANIO_ARG 
                    AND CAR_CARG_PERIODO = :PERIODO_ARG 
                    AND (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                    AND (CAR_1672_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
            ) T9 
            ON FT7.CAR_T1669_ID_MERCADO = T9.CAR_1672_ID_MERCADO 
            LEFT JOIN 
            (
                SELECT * FROM 
                (
                    SELECT VENTAS_TOTALES.*, VENTAS_REGULADOS.* FROM 
                    (
                        SELECT 
                            MERCADO AS MERCADO,
                            (SUM(VI_CAMPO20) + SUM(VR_CAMPO20)) AS C20,
                            (SUM(VI_CAMPO21) + SUM(VR_CAMPO21)) AS C21,
                            (SUM(VI_CAMPO22) + SUM(VR_CAMPO22)) AS C22,
                            (SUM(VI_CAMPO23) + SUM(VR_CAMPO23)) AS C23,
                            (SUM(VI_CAMPO24) + SUM(VR_CAMPO24)) AS C24,
                            (SUM(VI_CAMPO25) + SUM(VR_CAMPO25)) AS C25,
                            (SUM(VTI) + SUM(VTR)) AS C55 
                        FROM 
                        (
                            SELECT 
                                TO_NUMBER(SUBSTR(CAR_T1743_MERCADO_NIU, 1, INSTR(CAR_T1743_MERCADO_NIU, '-')-1)) AS MERCADO,
                                
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT = 1 AND CAR_T1743_TIPO_USU_RC = 1) THEN (CAR_T1743_CONS_USUARIO + CAR_T1743_CONS_CDC) END, 0) AS VI_CAMPO20,
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT = 1 AND CAR_T1743_TIPO_USU_RC = 2) THEN (CAR_T1743_CONS_USUARIO + CAR_T1743_CONS_CDC) END, 0) AS VI_CAMPO21,
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT = 1 AND CAR_T1743_TIPO_USU_RC = 3) THEN (CAR_T1743_CONS_USUARIO + CAR_T1743_CONS_CDC) END, 0) AS VI_CAMPO22,
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT = 1 AND CAR_T1743_TIPO_USU_RC = 4)  THEN (CAR_T1743_CONS_USUARIO + CAR_T1743_CONS_CDC) END, 0) AS VI_CAMPO23,
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT = 1 AND CAR_T1743_TIPO_USU_RC = 5) THEN (CAR_T1743_CONS_USUARIO + CAR_T1743_CONS_CDC) END, 0) AS VI_CAMPO24, 
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT = 1 AND CAR_T1743_TIPO_USU_RC = 6) THEN (CAR_T1743_CONS_USUARIO + CAR_T1743_CONS_CDC) END, 0) AS VI_CAMPO25,
                                
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT <> 1 AND CAR_T1743_TIPO_USU_RC = 1) THEN 
                                    CASE WHEN car_t1743_val_rft_cu >=0 THEN (CAR_T1743_RFT_CU*1) + CAR_T1743_RFT_CDC ELSE (CAR_T1743_RFT_CU*-1) + CAR_T1743_RFT_CDC END 
                                END, 0) AS VR_CAMPO20,
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT <> 1 AND CAR_T1743_TIPO_USU_RC = 2) THEN 
                                    CASE WHEN car_t1743_val_rft_cu >=0 THEN (CAR_T1743_RFT_CU*1) + CAR_T1743_RFT_CDC ELSE (CAR_T1743_RFT_CU*-1) + CAR_T1743_RFT_CDC END 
                                END, 0) AS VR_CAMPO21,
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT <> 1 AND CAR_T1743_TIPO_USU_RC = 3) THEN 
                                    CASE WHEN car_t1743_val_rft_cu >=0 THEN (CAR_T1743_RFT_CU*1) + CAR_T1743_RFT_CDC ELSE (CAR_T1743_RFT_CU*-1) + CAR_T1743_RFT_CDC END 
                                END, 0) AS VR_CAMPO22,
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT <> 1 AND CAR_T1743_TIPO_USU_RC = 4) THEN 
                                    CASE WHEN car_t1743_val_rft_cu >=0 THEN (CAR_T1743_RFT_CU*1) + CAR_T1743_RFT_CDC ELSE (CAR_T1743_RFT_CU*-1) + CAR_T1743_RFT_CDC END 
                                END, 0) AS VR_CAMPO23,
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT <> 1 AND CAR_T1743_TIPO_USU_RC = 5) THEN 
                                    CASE WHEN car_t1743_val_rft_cu >=0 THEN (CAR_T1743_RFT_CU*1) + CAR_T1743_RFT_CDC ELSE (CAR_T1743_RFT_CU*-1) + CAR_T1743_RFT_CDC END 
                                END, 0) AS VR_CAMPO24,
                                NVL(CASE WHEN (CAR_T1743_TIPO_FACT <> 1 AND CAR_T1743_TIPO_USU_RC = 6) THEN 
                                    CASE WHEN car_t1743_val_rft_cu >=0 THEN (CAR_T1743_RFT_CU*1) + CAR_T1743_RFT_CDC ELSE (CAR_T1743_RFT_CU*-1) + CAR_T1743_RFT_CDC END 
                                END, 0) AS VR_CAMPO25,
                                
                                NVL(CASE WHEN CAR_T1743_TIPO_FACT = 1 THEN (CAR_T1743_CONS_USUARIO + CAR_T1743_CONS_CDC) END, 0) AS VTI,
                        
                                NVL(CASE WHEN CAR_T1743_TIPO_FACT <> 1 THEN 
                                    CASE WHEN car_t1743_val_rft_cu >=0 THEN (CAR_T1743_RFT_CU*1) + CAR_T1743_RFT_CDC ELSE (CAR_T1743_RFT_CU*-1) + CAR_T1743_RFT_CDC END 
                                END, 0) AS VTR 
                            FROM ENERGIA_CREG_015.CAR_T1743_TC2FACTURACION_USU 
                            WHERE 
                                IDENTIFICADOR_EMPRESA = :EMPRESA_ARG 
                                AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS1 
                                AND CAR_CARG_ANO = :ANIO_ARG 
                        )
                        GROUP BY MERCADO
                    ) VENTAS_TOTALES,
                    (
                        SELECT MERCADO AS MERCADO_VR, (SUM(VRI) + SUM(VRR)) AS C60 FROM (
                        SELECT 
                            TO_NUMBER(SUBSTR(CAR_T1743_MERCADO_NIU, 1, INSTR(CAR_T1743_MERCADO_NIU, '-')-1)) AS MERCADO,
                            NVL(CASE WHEN CAR_T1743_TIPO_FACT = 1 THEN (CAR_T1743_CONS_USUARIO + CAR_T1743_CONS_CDC) END, 0) AS VRI,
                            NVL(CASE WHEN CAR_T1743_TIPO_FACT <> 1 THEN 
                                CASE WHEN car_t1743_val_rft_cu >=0 THEN (CAR_T1743_RFT_CU*1) + CAR_T1743_RFT_CDC ELSE (CAR_T1743_RFT_CU*-1) + CAR_T1743_RFT_CDC END 
                            END, 0) AS VRR 
                        FROM ENERGIA_CREG_015.CAR_T1743_TC2FACTURACION_USU 
                        WHERE 
                            IDENTIFICADOR_EMPRESA = :EMPRESA_ARG 
                            AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS2 
                            AND CAR_CARG_ANO = :ANIO_ARG 
                            AND CAR_T1743_TIPO_TARIFA = 1 
                        ) GROUP BY MERCADO
                    ) VENTAS_REGULADOS 
                    WHERE VENTAS_TOTALES.MERCADO = VENTAS_REGULADOS.MERCADO_VR
                ) VENTAS,
                (
                    SELECT 
                        CAR_T1732_ID_COMER,
                        CAR_T1732_ID_MERCADO,
                        COUNT(*) AS C59 FROM 
                    (
                        SELECT 
                            CAR_T1732_NIU,
                            CAR_T1732_ID_COMER,
                            CAR_T1732_ID_MERCADO 
                        FROM ENERGIA_CREG_015.CAR_T1732_TC1_INV_USUARIOS 
                        WHERE 
                            CAR_T1732_ID_COMER = :EMPRESA_ARG 
                            AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS2 
                            AND CAR_CARG_ANO = :ANIO_ARG 
                        GROUP BY 
                            CAR_T1732_NIU,
                            CAR_T1732_ID_COMER,
                            CAR_T1732_ID_MERCADO
                    ) TC1 
                    LEFT JOIN 
                    (
                        SELECT 
                            TO_NUMBER(SUBSTR(CAR_T1743_MERCADO_NIU, 1, INSTR(CAR_T1743_MERCADO_NIU, '-')-1)) AS MERCADO,
                            SUBSTR(CAR_T1743_MERCADO_NIU, INSTR(CAR_T1743_MERCADO_NIU, '-')+1) AS NIU 
                        FROM ENERGIA_CREG_015.CAR_T1743_TC2FACTURACION_USU 
                        WHERE 
                            IDENTIFICADOR_EMPRESA = :EMPRESA_ARG 
                            AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS2 
                            AND CAR_CARG_ANO = :ANIO_ARG 
                            AND CAR_T1743_TIPO_TARIFA = 1 
                        GROUP BY 
                            TO_NUMBER(SUBSTR(CAR_T1743_MERCADO_NIU, 1, INSTR(CAR_T1743_MERCADO_NIU, '-')-1)),
                            SUBSTR(CAR_T1743_MERCADO_NIU, INSTR(CAR_T1743_MERCADO_NIU, '-')+1)
                    ) TC2 
                    ON 
                        TC1.CAR_T1732_NIU = TC2.NIU 
                        AND TC1.CAR_T1732_ID_MERCADO = TC2.MERCADO 
                    WHERE TC2.NIU IS NOT NULL 
                    GROUP BY 
                        CAR_T1732_ID_COMER,
                        CAR_T1732_ID_MERCADO
                ) USUARIOS 
                WHERE VENTAS.MERCADO = USUARIOS.CAR_T1732_ID_MERCADO
            )FTC2 
            ON FT7.CAR_T1669_ID_MERCADO = FTC2.MERCADO 
            LEFT JOIN 
            (
                SELECT CERTIFICADO.QUA_EST_ESTADO, RUPS.*, FTE2.* FROM 
                (
                    SELECT 
                        VGSTR.* 
                    FROM 
                    (
                        SELECT TPG3.ID_MERCADO, VUTG.*, TPG3.TIPO_GARANTIA_3 AS C71 FROM 
                        (
                            SELECT 
                                FECHAS.*,
                                TPG1_2.TIPO_GARANTIA_1 AS C56,
                                TPG1_2.TIPO_GARANTIA_2 AS C69,
                                NVL(TPG1_2.TIPO_GARANTIA_2 / SUM_VENTAS_REGULADOS.SUMC60, 0) AS C70 
                            FROM 
                            (
                                SELECT ID_EMPRESA, NVL(TIPO_GARANTIA_1, 'SIN VALOR') AS FECHAS_TIPO_GARANTIA_1, NVL(TIPO_GARANTIA_2, 'SIN VALOR') AS FECHAS_TIPO_GARANTIA_2, NVL(TIPO_GARANTIA_3, 'SIN VALOR') AS FECHAS_TIPO_GARANTIA_3 FROM 
                                (
                                    SELECT ID_EMPRESA, CAR_T1667_TIPO_GARANTIA, VALOR FROM 
                                    (
                                        SELECT 
                                            ID_EMPRESA,
                                            CAR_T1667_TIPO_GARANTIA,
                                            CAR_T1667_MES_RECUPERACION,
                                            CAR_CARG_PERIODO,
                                            CASE WHEN CAR_T1667_MES_RECUPERACION > CAR_CARG_PERIODO THEN 'CUMPLE' ELSE 'NO CUMPLE' END AS VALOR 
                                        FROM 
                                            ENERGIA_CREG_015.CAR_GARANTIA_FINANCIERA 
                                        WHERE 
                                            CAR_CARG_ANO = :ANIO_ARG 
                                            AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS1 
                                            AND (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                                            AND CAR_T1667_TIPO_GARANTIA IN (1, 2, 3) 
                                    )
                                )
                                PIVOT 
                                (
                                    MAX(VALOR) 
                                    FOR 
                                        CAR_T1667_TIPO_GARANTIA 
                                    IN ('1' AS TIPO_GARANTIA_1, '2' AS TIPO_GARANTIA_2, '3' AS TIPO_GARANTIA_3) 
                                )
                            ) FECHAS,
                            (
                                SELECT ID_EMPRESA, NVL(TIPO_GARANTIA_1, 0) AS TIPO_GARANTIA_1, NVL(TIPO_GARANTIA_2, 0) AS TIPO_GARANTIA_2 FROM 
                                (
                                    SELECT 
                                        ID_EMPRESA,
                                        CAR_T1667_TIPO_GARANTIA,
                                        NVL(CASE WHEN CAR_T1667_TIPO_GARANTIA = 1 THEN SUM(CAR_T1667_COSTO_A_RECUPERAR) ELSE SUM(CAR_T1667_COSTO_A_RECUPERAR) END, 0) AS VALOR 
                                    FROM 
                                        ENERGIA_CREG_015.CAR_GARANTIA_FINANCIERA 
                                    WHERE 
                                        CAR_CARG_ANO = :ANIO_ARG 
                                        AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS1  
                                        AND (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                                        AND CAR_T1667_TIPO_GARANTIA IN (1, 2) 
                                    GROUP BY ID_EMPRESA, CAR_T1667_TIPO_GARANTIA
                                )
                                PIVOT 
                                (
                                    MAX(VALOR) 
                                    FOR 
                                        CAR_T1667_TIPO_GARANTIA 
                                    IN ('1' AS TIPO_GARANTIA_1, '2' AS TIPO_GARANTIA_2) 
                                )
                            ) TPG1_2,
                            (
                                SELECT 
                                    SUM(SUM_VENTAS_REGULADOS.VRI + SUM_VENTAS_REGULADOS.VRR) AS SUMC60 
                                FROM 
                                (
                                    SELECT MERCADO, NVL(SUM(VRI), 0) AS VRI, NVL(SUM(VRR), 0) AS VRR FROM (
                                    SELECT 
                                        TO_NUMBER(SUBSTR(CAR_T1743_MERCADO_NIU, 1, INSTR(CAR_T1743_MERCADO_NIU, '-')-1)) AS MERCADO,
                                        CASE WHEN CAR_T1743_TIPO_FACT = 1 THEN (CAR_T1743_CONS_USUARIO + CAR_T1743_CONS_CDC) END AS VRI,
                                        CASE WHEN CAR_T1743_TIPO_FACT <> 1 THEN 
                                            CASE WHEN car_t1743_val_rft_cu >=0 THEN (CAR_T1743_RFT_CU*1) + CAR_T1743_RFT_CDC ELSE (CAR_T1743_RFT_CU*-1) + CAR_T1743_RFT_CDC END 
                                        END AS VRR 
                                    FROM ENERGIA_CREG_015.CAR_T1743_TC2FACTURACION_USU 
                                    WHERE 
                                        IDENTIFICADOR_EMPRESA = :EMPRESA_ARG 
                                        AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS2 
                                        AND CAR_CARG_ANO = :ANIO_ARG 
                                        AND CAR_T1743_TIPO_TARIFA = 1 
                                    ) GROUP BY MERCADO
                                ) SUM_VENTAS_REGULADOS 
                            ) SUM_VENTAS_REGULADOS
                        ) VUTG,
                        (
                            SELECT MERCADOS.ID_MERCADO, MERCADOS.NOM_MERCADO, SUM(GRT3.TIPO_GARANTIA_3) AS TIPO_GARANTIA_3 FROM 
                            (
                                SELECT ID_EMPRESA, RUPS.ARE_ESP_SECUE, RUPS.ARE_ESP_NOMBRE, GARANTIAS3.CAR_T1667_NIT_BENEFICIARIO, GARANTIAS3.TIPO_GARANTIA_3 FROM 
                                (
                                    SELECT ID_EMPRESA, CAR_T1667_NIT_BENEFICIARIO, NVL(TIPO_GARANTIA_1, 0) AS TIPO_GARANTIA_1, NVL(TIPO_GARANTIA_2, 0) AS TIPO_GARANTIA_2, NVL(TIPO_GARANTIA_3, 0) AS TIPO_GARANTIA_3 FROM 
                                    (
                                        SELECT ID_EMPRESA, CAR_T1667_NIT_BENEFICIARIO, CAR_T1667_TIPO_GARANTIA, VALOR FROM 
                                        (
                                            SELECT 
                                                ID_EMPRESA,
                                                CAR_T1667_NIT_BENEFICIARIO,
                                                CAR_T1667_TIPO_GARANTIA,
                                                NVL(SUM(CAR_T1667_COSTO_A_RECUPERAR), 0) AS VALOR 
                                            FROM 
                                                ENERGIA_CREG_015.CAR_GARANTIA_FINANCIERA 
                                            WHERE 
                                                CAR_CARG_ANO = :ANIO_ARG 
                                                AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS1  
                                                AND (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                                            GROUP BY ID_EMPRESA, CAR_T1667_NIT_BENEFICIARIO, CAR_T1667_TIPO_GARANTIA
                                        )
                                    )
                                    PIVOT 
                                    (
                                        MAX(VALOR) 
                                        FOR 
                                            CAR_T1667_TIPO_GARANTIA 
                                        IN ('1' AS TIPO_GARANTIA_1, '2' AS TIPO_GARANTIA_2, '3' AS TIPO_GARANTIA_3) 
                                    )
                                ) GARANTIAS3,
                                (
                                    SELECT ARE_ESP_NOMBRE, ARE_ESP_SECUE, ARE_ESP_NIT FROM RUPS.ARE_ESP_EMPRESAS
                                ) RUPS 
                                WHERE GARANTIAS3.CAR_T1667_NIT_BENEFICIARIO = RUPS.ARE_ESP_NIT
                            ) GRT3,
                            (
                                SELECT 
                                    DISTINCT ID_MERCADO,
                                    ARE_ESP_SECUE,
                                    NOM_MERCADO,
                                    ESTADO 
                                FROM 
                                    CARG_COMERCIAL_E.MERCADO_EMPRESA 
                                WHERE 
                                    ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG 
                                    AND ESTADO = 'A' 
                                    AND NOM_MERCADO NOT LIKE '%Mercado Prueba%' 
                                    AND NOM_MERCADO NOT LIKE '%Mercado de Prueba%'  
                                UNION 
                                SELECT 
                                    20481 AS ID_MERCADO,
                                    20481 AS ARE_ESP_SECUE,
                                    'XM COMPANIA DE EXPERTOS EN MERCADOS S.A. E.S.P.' AS NOM_MERCADO,
                                    'A' AS ESTADO 
                                FROM DUAL
                            ) MERCADOS 
                            WHERE GRT3.ARE_ESP_SECUE = MERCADOS.ARE_ESP_SECUE 
                            GROUP BY MERCADOS.ID_MERCADO, MERCADOS.NOM_MERCADO 
                        ) TPG3
                    ) VGSTR
                ) FTE2,
                (
                    SELECT ARE_ESP_NOMBRE, ARE_ESP_SECUE, ARE_ESP_NIT FROM RUPS.ARE_ESP_EMPRESAS
                ) RUPS,
                (
                    SELECT CASE WHEN EXISTS (
                        SELECT 
                            QUA_EST_ESTADO 
                        FROM CALIDAD_SUI.FAC_QUA_ESTADO 
                        WHERE 
                            CAR_TIAR_CODIGO = '1667' 
                            AND ARE_ESP_SECUE = :EMPRESA_ARG 
                            AND EXTRACT(YEAR FROM QUA_EST_FCHCERT) = :ANIO_ARG 
                            AND EXTRACT(MONTH FROM QUA_EST_FCHCERT) = :PERIODO_ARG
                        ) 
                        THEN 'CERTIFICADO' ELSE 'NO CERTIFICADO' 
                        END AS QUA_EST_ESTADO 
                    FROM CALIDAD_SUI.FAC_QUA_ESTADO 
                    WHERE ROWNUM = 1
                ) CERTIFICADO
                WHERE FTE2.ID_EMPRESA = RUPS.ARE_ESP_SECUE
            ) FT2 
            ON FT7.CAR_T1669_ID_MERCADO = FT2.ID_MERCADO
        ) FORMATOS,
        (
            SELECT 
                CAR_T1671_CND AS C52,
                CAR_T1671_SIC AS C53 
            FROM ENERGIA_CREG_015.CAR_T1671_INFORMACION_ASIC_LAC 
            WHERE CAR_CARG_ANO = :ANIO_ARG 
            AND CAR_CARG_PERIODO = :PERIODO_ARG 
            AND (CAR_T1671_ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG)
        ) T10
'''