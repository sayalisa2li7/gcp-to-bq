function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.Pregnancies = values[0];
    obj.Glucose = values[1];
    obj.BloodPressure = values[2];
    obj.SkinThickness = values[3];
    obj.Insulin = values[4];
    obj.BMI = values[5];
    obj.DiabetesPedigreeFunction = values[6];
    obj.Age = values[7];
    obj.Outcome = values[8];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }