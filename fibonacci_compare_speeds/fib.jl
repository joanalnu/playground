function fib_benchmark()
    N = 1000000000 # 1 Billion
    a = UInt64(0)
    b = UInt64(1)

    # We run it once first to compile the function (ignoring JIT compilation overhead)
    # This ensures we only measure raw execution speed!
    time_taken = @elapsed begin
        for i in 1:N
            next = a + b
            a = b
            b = next
        end
    end

    println("Julia Result: ", a)
    println("Julia Time  : ", time_taken, " seconds")
end

fib_benchmark()
