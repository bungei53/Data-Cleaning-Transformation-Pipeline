import java.util.*;

public class DataValidator {
    public static class ValidationResult {
        public boolean isValid;
        public List<String> errors;

        public ValidationResult() {
            this.errors = new ArrayList<>();
        }
    }

    public ValidationResult validateRecord(Map<String, Object> record) {
        ValidationResult result = new ValidationResult();
        result.isValid = true;

        if (record.containsKey("age")) {
            int age = (int) record.get("age");
            if (age < 0 || age > 120) {
                result.isValid = false;
                result.errors.add("Age out of bounds: " + age);
            }
        }

        if (record.containsKey("cholesterol")) {
            double chol = (double) record.get("cholesterol");
            if (chol < 0) {
                result.isValid = false;
                result.errors.add("Negative cholesterol detected");
            }
        }

        return result;
    }

    public Map<String, ValidationResult> bulkValidate(List<Map<String, Object>> records) {
        Map<String, ValidationResult> results = new HashMap<>();
        for (Map<String, Object> record : records) {
            String id = (String) record.get("record_id");
            results.put(id, validateRecord(record));
        }
        return results;
    }
}
