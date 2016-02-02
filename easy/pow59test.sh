for i in {0..10}; do
    OBTAINED=$(echo ${i} | python pow59.py)
    CORRECT=$(echo ${i}^59 | bc)
    if [ $OBTAINED != $CORRECT ]
    then
        echo -e "Failed.\nExpected: $CORRECT\nGot: $OBTAINED"
        exit 1
    fi
done

echo "Tests passed!"
