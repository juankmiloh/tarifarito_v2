componenteR_sql = '''
    SELECT 
        T9_TC2.*,
        T10.*,
        (T10.C1 - T10.C2 + T10.C3 + T9_TC2.C4) AS C5,
        CASE WHEN T9_TC2.C6 <> 0 THEN (T10.C1 - T10.C2 + T10.C3 + T9_TC2.C4) / T9_TC2.C6 ELSE 0 END AS C7 
    FROM 
    (
        SELECT T9.*, NVL(TC2.C6, 0) AS C6 FROM
        (
            SELECT 
                ID_EMPRESA,
                CAR_1672_ID_MERCADO,
                CAR_CARG_ANO,
                CAR_CARG_PERIODO,
                CAR_1672_AREST AS C4 
            FROM 
                ENERGIA_CREG_015.CAR_VAR_COSTO_UNT_PS_CU_119_UR 
            WHERE 
                CAR_CARG_ANO = :ANIO_ARG 
                AND CAR_CARG_PERIODO = :PERIODO_ARG 
                AND (ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
                AND (CAR_1672_ID_MERCADO = :MERCADO_ARG OR 0 = :MERCADO_ARG) 
        ) T9
        LEFT JOIN
        (
            SELECT MERCADO AS MERCADO_VT, (SUM(VTI) + SUM(VTR)) AS C6 FROM (
            SELECT 
                TO_NUMBER(SUBSTR(CAR_T1743_MERCADO_NIU, 1, INSTR(CAR_T1743_MERCADO_NIU, '-')-1)) AS MERCADO,
                NVL(CASE WHEN CAR_T1743_TIPO_FACT = 1 THEN (CAR_T1743_CONS_USUARIO + CAR_T1743_CONS_CDC) END, 0) AS VTI,
                NVL(CASE WHEN CAR_T1743_TIPO_FACT <> 1 THEN 0 END , 0) AS VTR 
            FROM ENERGIA_CREG_015.CAR_T1743_TC2FACTURACION_USU 
            WHERE 
                IDENTIFICADOR_EMPRESA = :EMPRESA_ARG 
                AND CAR_CARG_PERIODO = :PERIODO_ARG_MENOS1 
                AND CAR_CARG_ANO = :ANIO_ARG  
            ) GROUP BY MERCADO
        ) TC2
        ON T9.CAR_1672_ID_MERCADO = TC2.MERCADO_VT
    ) T9_TC2,
    (
        SELECT 
            CAR_T1671_RTCSA AS C1,
            CAR_T1671_VDESV AS C2,
            CAR_T1671_GUATAPE AS C3 
        FROM ENERGIA_CREG_015.CAR_T1671_INFORMACION_ASIC_LAC 
        WHERE CAR_CARG_ANO = :ANIO_ARG 
        and CAR_CARG_PERIODO = :PERIODO_ARG 
        AND (CAR_T1671_ID_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
    ) T10
'''