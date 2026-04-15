FUNCTION fibonacci(n):
    IF n < 0 THEN
        RETURN "Error"
    ELSE IF n == 0 THEN
        RETURN 0
    ELSE IF n == 1 THEN
        RETURN 1
    ELSE
        RETURN fibonacci(n - 1) + fibonacci(n - 2)
    END IF
END FUNCTION