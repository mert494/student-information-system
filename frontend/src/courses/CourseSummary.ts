/** Proposed UI view model for #58; not an approved API or CourseOffering schema. */
export interface CourseSummary {
  readonly courseId: string;
  readonly courseCode: string;
  readonly title: string;
}

export type CourseListState =
  | { readonly status: 'loading' }
  | { readonly status: 'success'; readonly courses: readonly CourseSummary[] }
  | { readonly status: 'error'; readonly message?: string };
