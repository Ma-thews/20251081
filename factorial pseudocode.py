FUNCTION factorial(n):
    IF n < 0 THEN
        RETURN "Error"
    ELSE IF n == 0 OR n == 1 THEN
        RETURN 1
    ELSE
        RETURN n * factorial(n - 1)
    END IF
END FUNCTION